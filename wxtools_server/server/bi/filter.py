import django_filters
from .models import BusinessOrder

class OrderFilter(django_filters.FilterSet):
    class Meta():
        model = BusinessOrder
        fields = ['brand','billdate1']