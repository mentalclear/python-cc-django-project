""" Defines URL patters for pizzas """

from django.urls import path
from . import views

app_name ='pizzas'
urlpatterns = [
    # Home Page
    path('', views.index, name="index"),

    # The page that shows all pizzas
    path('pizzas/', views.pizzas, name='pizzas'),

    # The page that show all toppings for the pizza
    path('pizzas/<int:pizza_id>', views.pizza_id, name='pizza_id'),
]