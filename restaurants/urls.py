from django.urls import path
from .views import auth as auth_views
from .views import dashboard as dashboard_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', auth_views.MerchantLoginView.as_view(), name='merchant_login'),
    path('logout/', LogoutView.as_view(next_page='merchant_login'), name='merchant_logout'),
    path('dashboard/', dashboard_views.merchant_dashboard, name='merchant_dashboard'),
]