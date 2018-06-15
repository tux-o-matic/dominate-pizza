from django.shortcuts import render
from rest_framework import authentication, permissions, viewsets
from .models import Burger, Pizza
from .serializers import BurgerSerializer, PizzaSerializer


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


class PizzaViewSet(DefaultMixin, viewsets.ModelViewSet):
    queryset = Pizza.objects.order_by('name')
    serializer_class = PizzaSerializer
