from django.db import models

class Client(models.Model):
    cedula = models.IntegerField(unique=True)
    name = models.CharField(max_length=30, unique=True)

class Pizza(models.Model):
    name = models.CharField(max_length=30, unique=True)
    price = models.FloatField(default=1)

class Ingredient(models.Model):
    name = models.CharField(max_length=30, unique=True)
    price = models.FloatField(default=1)

class PizzaIngredient(models.Model):
    pizzaId = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    ingredientId = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

class OrderList(models.Model):
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    pizzaId = models.ForeignKey(Pizza, on_delete=models.CASCADE)

class ExtraIngredients(models.Model):
    OrderListId = models.ForeignKey(OrderList, on_delete=models.CASCADE)
    ingredientId = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
