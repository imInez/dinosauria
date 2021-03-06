from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

login_view = auth_views.LoginView.as_view(template_name='users/auth/login.html')
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/auth/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile')
]
