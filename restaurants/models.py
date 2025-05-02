from django.db import models
from .constants import PROTEIN_TYPE_CHOICES, US_STATE_CHOICES
from django.contrib.auth.models import User



# Create your models here.
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
    meal_type = models.CharField(
        max_length=20, 
        choices=[('main', 'Main'),('side', 'Side'),('drink', 'Drink')],
        default='main'
    )
    protein_grams = models.PositiveIntegerField(default=0)
    protein_type = models.ForeignKey('ProteinType', on_delete=models.CASCADE)
    veggie_grams = models.PositiveIntegerField(default=0)
    carb_grams = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name}, P:{self.protein_grams}, V:{self.veggie_grams}, C:{self.carb_grams}, Type:{self.meal_type}, PT:{self.protein_type}"
    
class ProteinType(models.Model):
    name = models.CharField(
        max_length=50, 
        choices=PROTEIN_TYPE_CHOICES,
        default='none'
    )

    def __str__(self):
        return self.get_name_display()
