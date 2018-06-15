from rest_framework import serializers
from . import models


class BurgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Burger
        fields = ('id', 'name', 'description',)


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Drink
        fields = ('id', 'name', 'description',)


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Meal
        fields = ('id', 'name', 'description',)


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pizza
        fields = ('id', 'name', 'description',)
