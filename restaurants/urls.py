from django.urls import path
from . import views as merchant_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='merchant/login.html'), name='merchant_login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='merchant_login'), name='merchant_logout'),
    path('dashboard/', merchant_views.merchant_dashboard, name='merchant_dashboard'),
]