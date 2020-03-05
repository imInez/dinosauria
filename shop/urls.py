from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('products/<int:id>/<slug:slug>', views.product_details, name='product_details'),
    path('products/', views.products, name='products'),
    path('', views.home, name='home')
]