import django_filters
from rest_framework import filters
from index.models import CartModel


class CartFilter(filters.FilterSet):
    goods = django_filters.CharFilter('goods')
    user = django_filters.CharFilter('user')

    class Meta:
        model = CartModel
        fields = ['goods', 'user']