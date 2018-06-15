from rest_framework import serializers
from . import models


class BurgerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Burger
        fields = ('id', 'url', 'name', 'description',
                  'price',)


class DrinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Drink
        fields = ('id', 'url', 'name', 'description',
                  'price',)


class MealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Meal
        fields = ('id', 'url', 'name', 'description',
                  'price',)


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Menu
        fields = ('id', 'url', 'name', 'description',
                  'price',)


class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Pizza
        fields = ('id', 'url', 'name', 'description',
                  'diameter', 'currency', 'organic', 'price', 'vat', 'vegetarian')
