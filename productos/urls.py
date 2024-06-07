#from django.urls import path
from .views import CategoriaViewSet, ProductoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('productos', ProductoViewSet, basename='productos' )
router.register('categoria', CategoriaViewSet, basename='categoria' )


urlpatterns = router.urls