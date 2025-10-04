from django.db import models
from .constants import US_STATE_CHOICES
from django.contrib.auth.models import User
  


class Restaurant(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurants')
    name = models.CharField(max_length=200)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20, choices=US_STATE_CHOICES)
    zip_code = models.IntegerField()
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name
    
class Item(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='dish_photos/')
    protein_grams = models.PositiveIntegerField(default=0)
    veggie_grams = models.PositiveIntegerField(default=0)
    carb_grams = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    meal_ready_time = models.PositiveIntegerField()
    tag = models.ManyToManyField('Tag', related_name='items')


class Tag(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}: {self.category}"
