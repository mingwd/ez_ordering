from django import forms
from .models import Item

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'name',
            'image',
            'meal_type',
            'protein_type',
            'protein_grams',
            'veggie_grams',
            'carb_grams',
            'price'
        ]

from django.contrib.auth.models import User
from .models import Restaurant

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'street_address',
            'city',
            'state',
            'zip_code',
            'lat',
            'lng',
        ]