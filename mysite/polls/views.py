from django.http import HttpResponse
from polls.models import Pizza
from polls.models import Ingredient
from polls.forms import PizzaForm
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def set8Pizzas(request):
    pizza = Pizza (name = 'Margarita')
    pizza.save()
    
    pizza = Pizza (name = 'Cuatro Quesos')
    pizza.save()

    pizza = Pizza (name = 'Pepperoni')
    pizza.save()

    pizza = Pizza (name = 'Cuatro Estaciones')
    pizza.save()

    pizza = Pizza (name = 'Champiñones')
    pizza.save()

    pizza = Pizza (name = 'Hawaiana')
    pizza.save()

    pizza = Pizza (name = 'Marinara')
    pizza.save()

    pizza = Pizza (name = 'Neo-yorquina')
    pizza.save()

    pizza = Pizza (name = 'Fugazza')
    pizza.save() 

    return HttpResponse("8 pizas han sido creadas")

@csrf_exempt
def AllPizzas(request):
    pizzas = Pizza.objects.all()

    json_data = serializers.serialize('json', pizzas)
    return HttpResponse( json_data )

@csrf_exempt
def AllPizzas(request):
    ingredientes = Ingredient.objects.all()

    json_data = serializers.serialize('json', ingredientes)
    return HttpResponse( json_data )

@csrf_exempt
def setIngredients(request):
    ingrediente = Ingredient (name = 'Queso Mozzarella', price = 2)
    ingrediente.save()

    ingrediente = Ingredient (name = 'Tomate', price = 1)
    ingrediente.save()

    ingrediente = Ingredient (name = 'Salsa', price = 3)
    ingrediente.save()

    ingrediente = Ingredient (name = 'Queso Gorgonzola', price = 3)
    ingrediente.save()

    ingrediente = Ingredient (name = 'Queso Roquefort', price = 3)
    ingrediente.save()

    ingrediente = Ingredient (name = 'Queso Padano', price = 3)
    ingrediente.save()

    ingrediente = Ingredient (name = 'Queso Parmesano', price = 3)
    ingrediente.save()

    ingrediente = Ingredient (name = 'Queso Ricotta', price = 3)
    ingrediente.save()

    ingrediente = Ingredient (name = 'Queso Salami', price = 3)
    ingrediente.save()

    ingrediente = Ingredient (name = 'Queso Mortadela', price = 3)
    ingrediente.save()
    
    ingrediente = Ingredient (name = 'Coppa Piacentina', price = 3)
    ingrediente.save()

    ingrediente = Ingredient (name = 'Prosciutto', price = 3)
    ingrediente.save()

    ingrediente = Ingredient (name = 'Pepperoni', price = 3)
    ingrediente.save()

    ingrediente = Ingredient (name = 'Aceitunas Negras', price = 3)
    ingrediente.save()

    ingrediente = Ingredient (name = 'Cebollas', price = 3)
    ingrediente.save()

    return HttpResponse("Ingredientes han sido creados")

