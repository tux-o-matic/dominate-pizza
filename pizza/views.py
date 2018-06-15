from django.shortcuts import render
from rest_framework import authentication, permissions, viewsets
from .models import Burger, Drink, Meal, Menu, Pizza
from .serializers import BurgerSerializer, DrinkSerializer, MealSerializer, MenuSerializer, PizzaSerializer


def index(request):
    return render(
        request,
        'index.html',
    )


class DefaultMixin(object):
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class RestrictedtMixin(object):
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class BurgerViewSet(DefaultMixin, viewsets.ModelViewSet):
    queryset = Burger.objects.order_by('name')
    serializer_class = BurgerSerializer


class DrinkViewSet(DefaultMixin, viewsets.ModelViewSet):
    queryset = Drink.objects.order_by('name')
    serializer_class = DrinkSerializer


class MealViewSet(DefaultMixin, viewsets.ModelViewSet):
    queryset = Meal.objects.order_by('name')
    serializer_class = MealSerializer


class MenuViewSet(DefaultMixin, viewsets.ModelViewSet):
    queryset = Menu.objects.order_by('name')
    serializer_class = MenuSerializer


class PizzaViewSet(DefaultMixin, viewsets.ModelViewSet):
    queryset = Pizza.objects.order_by('name')
    serializer_class = PizzaSerializer
