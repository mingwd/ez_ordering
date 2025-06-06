from django.urls import path
from .views import auth as auth_views
from .views import dashboard as dashboard_views
from .views import add_item as add_item_views
from .views import add_restaurant as add_restaurant_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', auth_views.MerchantLoginView.as_view(), name='merchant_login'),
    path('logout/', LogoutView.as_view(next_page='merchant_login'), name='merchant_logout'),
    path('dashboard/', dashboard_views.merchant_dashboard, name='merchant_dashboard'),
    path('restaurant/<int:restaurant_id>/add-item/', add_item_views.add_item_view, name='add_item'),
    path('restaurant/<int:id>/', dashboard_views.restaurant_dashboard, name='restaurant_dashboard'),
    path('signup/', auth_views.merchant_signup_view, name='merchant_signup'),
    path('add-restaurant/', add_restaurant_views.add_restaurant_view, name='add_restaurant')
]