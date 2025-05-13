from django.db import models
from django.contrib.auth.models import User
from restaurants.models import Tag

class CustomerPreference(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='customers')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('user', 'tag')

class CustomerProfile(models.Model):
    ACTIVITY_LEVEL_CHOICES = [
        ('office', 'Office'),
        ('active', 'Active'),
        ('athlete', 'Athlete'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male'), 
        ('female', 'Female')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    height_cm = models.PositiveIntegerField()
    weight_kg = models.PositiveIntegerField()
    activity_level = models.CharField(
        max_length=10,
        choices=ACTIVITY_LEVEL_CHOICES,
        default = 'office'
    )
    bmr = models.FloatField(editable=False, null=True, blank=True)
    
    def calculate_bmr(self):
        if self.gender == 'male':
            return 10 * self.weight_kg + 6.25 * self.height_cm - 5 * self.age + 5
        elif self.gender == 'female':
            return 10 * self.weight_kg + 6.25 * self.height_cm - 5 * self.age - 161

    def get_calorie_range(self):
        multiplier = {
            'office': 1.2,
            'active': 1.55,
            'athlete': 1.75,
        }.get(self.activity_level, 1.2)

        tdee = self.bmr * multiplier
        return round(tdee * 0.95), round(tdee * 1.05)

    def save(self, *args, **kwargs):
        self.bmr = self.calculate_bmr()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s profile"