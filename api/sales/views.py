from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Avg, Count, F
from django.db.models.functions import TruncDate
from .models import Sale
from customers.models import Customer


class SalesStatisticsView(APIView):
    """
    API view for sales statistics.
    Returns daily sales totals.
    """
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        """
        Get total sales amount grouped by day.
        """
        daily_sales = (
            Sale.objects
            .values('sale_date')
            .annotate(total=Sum('amount'))
            .order_by('sale_date')
        )
        
        statistics = []
        for sale in daily_sales:
            statistics.append({
                'date': sale['sale_date'].strftime('%Y-%m-%d'),
                'total': float(sale['total'])
            })
        
        return Response({
            'daily_sales': statistics
        })


class CustomerStatisticsView(APIView):
    """
    API view for customer-specific statistics.
    Returns top customers by different metrics.
    """
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        """
        Get customer statistics including:
        - Customer with highest sales volume
        - Customer with highest average sale value
        - Customer with highest purchase frequency
        """
        
        top_volume_customer = (
            Customer.objects
            .annotate(total_sales=Sum('sales__amount'))
            .exclude(total_sales__isnull=True)
            .order_by('-total_sales')
            .first()
        )
        
        top_average_customer = (
            Customer.objects
            .annotate(avg_sale=Avg('sales__amount'))
            .exclude(avg_sale__isnull=True)
            .order_by('-avg_sale')
            .first()
        )
        
        top_frequency_customer = (
            Customer.objects
            .annotate(unique_days=Count('sales__sale_date', distinct=True))
            .exclude(unique_days=0)
            .order_by('-unique_days')
            .first()
        )
        
        response_data = {}
        
        if top_volume_customer:
            response_data['highest_volume'] = {
                'customer': {
                    'id': top_volume_customer.id,
                    'full_name': top_volume_customer.full_name,
                    'email': top_volume_customer.email
                },
                'total_sales': float(top_volume_customer.total_sales)
            }
        
        if top_average_customer:
            response_data['highest_average'] = {
                'customer': {
                    'id': top_average_customer.id,
                    'full_name': top_average_customer.full_name,
                    'email': top_average_customer.email
                },
                'average_sale': float(top_average_customer.avg_sale)
            }
        
        if top_frequency_customer:
            response_data['highest_frequency'] = {
                'customer': {
                    'id': top_frequency_customer.id,
                    'full_name': top_frequency_customer.full_name,
                    'email': top_frequency_customer.email
                },
                'unique_purchase_days': top_frequency_customer.unique_days
            }
        
        return Response(response_data)