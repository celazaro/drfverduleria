from rest_framework import serializers  # type: ignore
from django_filters import rest_framework as filters

from .models import Categoria, Productos

class ProductoFilter(filters.FilterSet):
    
    categoria = filters.NumberFilter(field_name='categora', lookup_expr='exact')
    nombre = filters.CharFilter(method='filter_by_search', lookup_expr='icontains')
    
    def filter_by_search (self, queryset, value):
        return queryset.filter( name__icontains = value ) | queryset.filter( descripcion__icontains = value )
    
    class Meta:
        model = Productos
        fields = ['categoria', 'nombre',]
""" 
En caso que no funcione el código anterior habría que usar:
        fields = [
            'categoria' : ['exact'],
            'nombre' : ['icontains'],
        ]
 """

class ProductoSerializers(serializers.ModelSerializer):
    categoria_nombre = serializers.ReadOnlyField(source='categoria.nombre')
    precio_tipo_descripcion = serializers.ReadOnlyField(source='get_precio_tipo_display')
    class Meta:
        model=Productos
        fields = ['id', 'nombre', 'imagen', 'categoria', 'categoria_nombre', 'descripcion', 'precio', 'precio_tipo', 'precio_tipo_descripcion']
        filterset_class = ProductoFilter
        
        
class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields = ['id', 'nombre']