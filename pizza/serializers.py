from rest_framework import serializers
from . import models


class BurgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Burger
        fields = ('id', 'name', 'description', 'price',)


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Drink
        fields = ('id', 'name', 'description', 'price',)


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Meal
        fields = ('id', 'name', 'description', 'price',)


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Menu
        fields = ('id', 'name', 'description', 'price',)


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pizza
        fields = ('id', 'name', 'description', 'price',)
