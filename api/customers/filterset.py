from customers.models import Customer
from django_filters import rest_framework as filters


class CustomerFilterSet(filters.FilterSet):
    full_name = filters.CharFilter(field_name="full_name", lookup_expr="icontains")
    email = filters.CharFilter(field_name="email", lookup_expr="icontains")

    class Meta:
        model = Customer
        fields = ["full_name", "email"]