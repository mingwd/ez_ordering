from django.urls import path
from .views import customer_login_view
from .views import customer_dashboard_view
from .views import customer_signup_view
from .views import customer_login_error_view
from .views import customer_profile_edit_view

from .views import frontend_login_view


urlpatterns = [
    path('login/', customer_login_view, name='customer_login'),
    path('customer-dashboard/', customer_dashboard_view, name='customer_dashboard'),
    path('signup/', customer_signup_view, name='customer_signup'),
    path('profile/edit/', customer_profile_edit_view, name='customer_profile_edit'),
    path('login-error', customer_login_error_view, name='login_error'),
    path('f-login/', frontend_login_view)
]