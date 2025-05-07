from django.contrib import admin

# Register your models here.
from .models import Restaurant, Item, Tag, CustomerPreference

admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(Tag)
admin.site.register(CustomerPreference)