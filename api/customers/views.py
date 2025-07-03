from rest_framework import viewsets, permissions
from .models import Customer
from rest_framework import generics
from rest_framework.response import Response
from .serializers import CustomerSerializer, CustomerCreateSerializer, CustomerListSerializer
from .filterset import CustomerFilterSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_class = CustomerFilterSet
    search_fields = ['full_name', 'email']
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return CustomerListSerializer
        if self.action == 'create':
            return CustomerCreateSerializer
        return CustomerSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page if page is not None else queryset, many=True)
        response_data = {
            "data": {
                "clientes": serializer.data
            },
            "meta": {
                "registroTotal": queryset.count(),
                "pagina": self.paginator.page.number if page is not None else 1
            },
            "redundante": {
                "status": "ok"
            }
        }
        if page is not None:
            return self.get_paginated_response(response_data)
        return Response(response_data)


class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def destroy(self, request, *args, **kwargs):
     
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Cliente removido com sucesso."},
            status=200
        )