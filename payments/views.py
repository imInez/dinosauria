from django.shortcuts import render
from orders.models import Order
from django.shortcuts import get_object_or_404, redirect
import braintree


def payment(request):
    order = get_object_or_404(Order, id=request.session.get('order_id'))
    order.status = 'PAYONG'
    if request.method == 'POST':
        token = request.POST.get('payment_method_nonce', None)
        result = braintree.Transaction.sale({
            'amount': order.total,
            'payment_method_nonce': token,
            'options': {
                'submit_for_settlement': True
            }
        })
        if result.is_success:
            order.payment_status = 'S'
            order.status = 'PAYPRO'
            order.payment_id = result.transaction.id
            order.save()

            return redirect('payments:success')
        else:
            for error in result.errors.errors:
                print('ERROR: ', error)
                print(error.attribute)
                print(error.code)
                print(error.message)
            for error in result.errors.deep_errors:
                print('DEEP ERROR: ', error)
                print(error.attribute)
                print(error.code)
                print(error.message)

            return redirect('payments:failure')
    else:
        client_token = braintree.ClientToken.generate()
        return render(request, 'payments/payment.html', {'order': order, 'client_token': client_token})


def payment_success(request):
    return render(request, 'payments/success.html')


def payment_failure(request):
    return render(request, 'payments/failure.html')