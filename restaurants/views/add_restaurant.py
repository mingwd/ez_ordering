from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import RestaurantForm

@login_required
def add_restaurant_view(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.owner = request.user
            new_item.save()
            return redirect('merchant_dashboard')
    else:
        form = RestaurantForm()

    return render(request, 'merchant/add_restaurant.html', {'form': form})