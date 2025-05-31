from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from restaurants.forms import AddItemForm
from restaurants.models import Restaurant

@login_required
def add_item_view(request, restaurant_id):

    restaurant = Restaurant.objects.get(id=restaurant_id, owner=request.user)

    if request.method == 'POST':
        form = AddItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(restaurant=restaurant)
            return redirect('merchant_dashboard')
    else:
        form = AddItemForm()

    return render(request, 'merchant/add_item.html', {'form': form})