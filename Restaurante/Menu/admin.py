from django.contrib import admin
from Menu.models import Menu, Categoria_platillo, Mesero, Orden, Mesa, Perfil


# Register your models here.
admin.site.register(Menu)
admin.site.register(Categoria_platillo)
admin.site.register(Mesero)
admin.site.register(Orden)
admin.site.register(Mesa)
admin.site.register(Perfil)