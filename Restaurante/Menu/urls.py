from django.urls import path
from Menu import views
from .views import show_food, load_menu, busqueda,show_administrador, show_cliente


urlpatterns = [
    path('/', views.show_food),
    path('base_menu/', views.base, name='base_menu'),
    path('cargar_catalogo/', views.load_menu, name='load_menu'),
    path('busqueda/', views.busqueda, name='busqueda'),  
    path('administrador/', views.show_administrador, name='administrador'),
    path('cliente/', views.show_cliente, name='cliente'),  
]