from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']
        
    def __str__(self):
        return self.nombre


class Productos(models.Model):
    precio_type_choices = (
        ('unitario', 'Precio Unitario'),
        ('media-doc', 'Media Docena'),
        ('docena', 'Docena'),
        ('por-kilo', 'Kilo')
    )
    
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    imagen = models.ImageField(upload_to='productos', default='imagen_default.png', verbose_name='Imagen')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='get_products', verbose_name='Categoría')
    descripcion = models.TextField(verbose_name='Descripción')
    precio = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Precio')
    precio_tipo = models.CharField(max_length=9, choices=precio_type_choices, default='unitario', verbose_name='Tipo de Precio')
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']
        
    def __str__(self):
        return self.nombre