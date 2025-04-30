from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class MerchantLoginView(LoginView):
    template_name='merchant/login.html'
    redirect_authenticated_user=True
    success_url=reverse_lazy('merchant_dashboard')