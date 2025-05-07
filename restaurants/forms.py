from django import forms
from .models import Item, Tag

class AddItemForm(forms.ModelForm):
    tag_cuisine = forms.ModelChoiceField(queryset=Tag.objects.filter(category='Cuisine'), required=False)
    tag_protein = forms.ModelChoiceField(queryset=Tag.objects.filter(category='Protein'), required=False)
    tag_spiciness = forms.ModelChoiceField(queryset=Tag.objects.filter(category='Spiciness'), required=False)
    tag_mealtype = forms.ModelChoiceField(queryset=Tag.objects.filter(category='MealType'), required=False)
    tag_flavor = forms.ModelChoiceField(queryset=Tag.objects.filter(category='Flavor'), required=False)
    tag_allergen = forms.ModelChoiceField(queryset=Tag.objects.filter(category='Allergen'), required=False)
    tag_nutrition = forms.ModelChoiceField(queryset=Tag.objects.filter(category='Nutrition'), required=False)
    
    class Meta:
        model = Item
        fields = [
            'name',
            'image',
            'protein_grams',
            'veggie_grams',
            'carb_grams',
            'price',
            'meal_ready_time'
        ]
        unique_together = ('name', 'category')
    
    def save(self, restaurant, commit=True):
        instance = super().save(commit=False)
        instance.restaurant = restaurant
        instance.save()

        selected_tags = [
            self.cleaned_data.get('tag_cuisine'),
            self.cleaned_data.get('tag_protein'),
            self.cleaned_data.get('tag_spiciness'),
            self.cleaned_data.get('tag_mealtype'),
            self.cleaned_data.get('tag_flavor'),
            self.cleaned_data.get('tag_allergen'),
            self.cleaned_data.get('tag_nutrition'),
        ]
        # filter None field
        for tag in filter(None, selected_tags):
            instance.tag.add(tag)
        return instance

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
