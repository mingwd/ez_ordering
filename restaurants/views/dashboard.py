from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from restaurants.models import Restaurant

@login_required
def merchant_dashboard(request):

    restaurants = request.user.restaurants.all()
    return render(request, 'merchant/dashboard.html',{
        'user': request.user,
        'restaurants': restaurants
    })

def restaurant_dashboard(request, id):
    restaurant = Restaurant.objects.get(id=id, owner=request.user)
    items = restaurant.items.all()
    return render(request, 'merchant/restaurant_dashboard.html', {
        'restaurant': restaurant,
        'items': items
    })