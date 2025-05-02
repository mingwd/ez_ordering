from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class MerchantLoginView(LoginView):
    template_name='merchant/login.html'
    redirect_authenticated_user=True
    success_url=reverse_lazy('merchant_dashboard')


from django.contrib.auth import login
from django.shortcuts import render, redirect
from restaurants.forms import UserForm, RestaurantForm



def merchant_signup_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        restaurant_form = RestaurantForm(request.POST)

        if user_form.is_valid() and restaurant_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            restaurant = restaurant_form.save(commit=False)
            restaurant.owner = user
            restaurant.save()

            login(request, user)
            return redirect('merchant_dashboard')

    else:
        user_form = UserForm()
        restaurant_form = RestaurantForm()
    
    return render(request, 'merchant/signup.html', {
        'user_form': user_form,
        'restaurant_form': restaurant_form
    })