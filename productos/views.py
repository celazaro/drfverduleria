from rest_framework import viewsets
from rest_framework.decorators import action 
from rest_framework.response import Response

from .models import Categoria, Productos 
from .serializers import CategoriaSerializers, ProductoSerializers 

class CategoriaViewSet (viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers

class ProductoViewSet (viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductoSerializers
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filtrado por Categoría
        categoria = self.request.query_params.get('categoria')
        if categoria:
            queryset = queryset.filter(categoria = categoria)
        
        # Filtrado por nombre de producto
        search = self.request.query_params.get('search', None)
        if search is not None:
            queryset = queryset.filter(nombre__icontains = search) | queryset.filter(descripcion__icontains = search )
        
        return queryset

    """ @action(detail=False)
    def por_categoria(self, request):
        categoria = self.request.query_params.get('categoria', None)
        producto = Productos.objects.filter(categoria=categoria)
        serializer = ProductoSerializers(producto, many=True)
        return Response (serializer.data) """
    
    