from django.shortcuts import render

def index(request):
    """ Home page for Pizzas """
    return render(request, 'pizzas/index.html')
