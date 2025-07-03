from django.urls import path
from .views import SalesStatisticsView, CustomerStatisticsView

urlpatterns = [
    path('sales/statistics/', SalesStatisticsView.as_view(), name='sales-statistics'),
    path('sales/customers/statistics/', CustomerStatisticsView.as_view(), name='customer-statistics'),
] 