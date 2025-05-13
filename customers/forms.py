from django.contrib.auth.models import User
from django import forms
from .models import CustomerProfile
from restaurants.models import Tag

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = [
            'height_cm', 'weight_kg', 'activity_level', 'gender', 'age'
        ]

class CustomerTagForm(forms.Form):
    preference_tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )