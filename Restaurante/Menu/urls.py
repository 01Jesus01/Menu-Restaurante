from django.urls import path
from Menu import views
from .views import show_food, load_menu, busqueda,show_administrador,show_cocina,show_mesero,show_cliente


urlpatterns = [
    path('/', views.show_food),
    path('base_menu/', views.base, name='base_menu'),
    path('cargar_catalogo/', views.load_menu, name='load_menu'),
    path('busqueda/', views.busqueda, name='busqueda'),
    path('administrador/', views.show_administrador, name='administrador'),
    path('cocina/', views.show_cocina, name='cocina'),
    path('mesero/', views.show_mesero, name='administrador'),
    path('cliente/', views.show_cliente, name='cliente'),
]