from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from restaurants.forms import AddItemForm
from restaurants.models import Restaurant

@login_required
def add_item(request):
    restaurant = Restaurant.objects.first()

    if request.method == 'POST':
        form = AddItemForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.restaurant = restaurant
            new_item.save()
            return redirect('merchant_dashboard')
    else:
        form = AddItemForm()

    return render(request, 'merchant/add_item.html', {'form': form})