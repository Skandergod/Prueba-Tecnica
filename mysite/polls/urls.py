from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [

    path("", views.index, name="index"),
    path("set8Pizzas", views.set8Pizzas, name="set8Pizzas"),
    path("setIngredients", views.setIngredients, name="setIngredients"),
    path("allPizzas", views.AllPizzas, name="AllPizzas"),

]