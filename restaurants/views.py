from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def merchant_dashboard(request):
    user = request.user
    return render(request, 'merchant/dashboard.html', {'user': user})