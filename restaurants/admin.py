from django.contrib import admin

# Register your models here.
from .models import Restaurant, Item, ProteinType

admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(ProteinType)