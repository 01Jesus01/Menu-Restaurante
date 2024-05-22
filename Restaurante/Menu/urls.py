from django.urls import path
from Menu import views
from .views import show_food, load_menu, busqueda,show_administrador,show_cocina,show_mesero,show_cliente,orden_view


urlpatterns = [
    path('/', views.show_food),
    path('base_menu/', views.base, name='base_menu'),
    path('cargar_catalogo/', views.load_menu, name='load_menu'),
    path('busqueda/', views.busqueda, name='busqueda'),  
    path('administrador/', views.show_administrador, name='administrador'),
    path('cocina/', views.show_cocina, name='cocina'),
    path('mesero/', views.show_mesero, name='administrador'),
    path('cliente/', views.show_cliente, name='cliente'),    
    path('modificar_menu/<int:id>/', views.modificar_menu, name='modificar_menu'),
    path('eliminar_menu/<int:id>/', views.eliminar_menu, name='eliminar_menu'),
    path('orden/', views.orden_view, name='orden'), 

]