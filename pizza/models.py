from django.db import models


class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(default=None, blank=True, max_length=255, null=True)

    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    vat = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    currency = models.CharField(default='EUR', max_length=3)

    organic = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Burger(Product):
    bacon = models.BooleanField(default=False)
    cheese = models.BooleanField(default=False)
    steaks = models.SmallIntegerField(default=0)
    others = models.CharField(max_length=255)


class Meal(Product):
    pass


class Topping(Product):
    pass


class Pizza(Product):
    calzone = models.BooleanField(default=False)
    diameter = models.SmallIntegerField(default=0)

    toppings = models.ManyToManyField(Topping)


class Drink(Product):
    size = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    alcohol = models.BooleanField(default=False)


class Menu(models.Model):
    # inherited price is expected to be cheaper than sum of items in menu
    burgers = models.ManyToManyField(Burger, blank=True)
    drinks = models.ManyToManyField(Drink, blank=True)
    meals = models.ManyToManyField(Meal, blank=True)
    pizzas = models.ManyToManyField(Pizza, blank=True)


class Order(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    placed_on = models.DateTimeField(auto_now_add=True)
    shipped_on = models.DateTimeField(auto_now_add=True)

    burgers = models.ManyToManyField(Burger, blank=True)
    drinks = models.ManyToManyField(Drink, blank=True)
    meals = models.ManyToManyField(Meal, blank=True)
    menus = models.ManyToManyField(Menu, blank=True)
    pizzas = models.ManyToManyField(Pizza, blank=True)


