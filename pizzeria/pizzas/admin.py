from django.contrib import admin

# Importing the models:
from .models import Pizza, Topping

admin.site.register(Pizza)
admin.site.register(Topping)
