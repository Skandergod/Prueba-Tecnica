# Generated by Django 5.0.4 on 2024-04-16 22:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_pizza_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('price', models.FloatField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.client')),
            ],
        ),
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.order')),
                ('pizzaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.pizza')),
            ],
        ),
        migrations.CreateModel(
            name='ExtraIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.ingredient')),
                ('OrderListId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.orderlist')),
            ],
        ),
        migrations.CreateModel(
            name='PizzaIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.ingredient')),
                ('pizzaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.pizza')),
            ],
        ),
    ]
