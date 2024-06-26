from django.urls import path
from django.contrib.auth import views as auth_views
from Menu import views
from .views import base, index, load_menu, busqueda,show_administrador,show_cocina,show_mesero,show_cliente,show_orden, registro, login_view, show_categoria, show_orden2, crear_orden, update_order_status
from .views import insertar_valores_orden, logout_view,crear_orden

urlpatterns = [
    path('', views.show_cliente, name='cliente'),
    path('index/', views.index, name='base'),
    path('base_menu/', views.base, name='base_menu'),
    path('cargar_catalogo/', views.load_menu, name='load_menu'),
    path('busqueda/', views.busqueda, name='busqueda'),  
    path('administrador/', views.show_administrador, name='administrador'),
    path('cocina/', views.show_cocina, name='cocina'),
    path('mesero/', views.show_mesero, name='administrador'),
    path('orden/', views.show_orden, name='orden'), 
    # path('registro/', registro, name='registro'),
    # path('login/', login_view, name='login'),
    path('categoria/<int:opcion>/', views.show_categoria, name='categoria'),
    path('comprobante/', views.show_orden2, name='comprobante'),
    path('crear_orden/', views.crear_orden, name='crear_orden'),
    path('insertar_valores_orden/', views.insertar_valores_orden, name='insertar_valores_orden'),
    path('update_order_status/', update_order_status, name='update_order_status'),
    #path('login/', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro, name='registro'),

]