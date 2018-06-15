from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    price = models.DecimalField(..., max_digits=5, decimal_places=2)
    currency = models.CharField(max_length=2)

    organic = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Burger(Food):
    bacon = models.BooleanField(default=False)
    cheese = models.BooleanField(default=False)
    steaks = models.SmallIntegerField(default=0)
    others = models.CharField(max_length=255)


class Meal(Food):
    pass

class Topping(Food):
    pass


class Pizza(Food):
    calzone = models.BooleanField()
    diameter = models.SmallIntegerField(default=0)

    toppings = models.ManyToManyField(Topping)


class Drink(Food):
    size = models.DecimalField(..., max_digits=3, decimal_places=2)
    alcohol = models.BooleanField(default=False)


