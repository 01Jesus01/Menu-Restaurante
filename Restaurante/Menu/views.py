from django.shortcuts import render, redirect
from Menu.models import Menu, Mesa, Orden, Categoria_platillo, Mesero # Importa tu modelo Menu
from . import forms
from .forms import Form_Comments
from django.http import JsonResponse

def show_food(request):
    # Obtén todas las Platillos guardadas
    platillos = Menu.objects.all()
    
    # Verifica si se está realizando una búsqueda
    if 'q' in request.GET:
        query = request.GET.get('q')
        try:
            platillo = Menu.objects.get(Nombre__iexact=query)
            resultados = [{'Platillo': platillo.Nombre, 'Categoria': platillo.categoria}]
            return JsonResponse(resultados, safe=False)
        except Menu.DoesNotExist:
            # Handle the case when no matching Menu object is found
            resultados = [{'Platillo': 'No se encontraron resultados'}]
            return JsonResponse(resultados, safe=False)
    
    # Si no hay búsqueda, renderiza la plantilla con todas las platillos
    return render(request, 'Menu/index.html', {'platillos': platillos})


def busqueda(request):
    Platillo_seleccionado = None  # Inicializa la variable en caso de que no se encuentre ningún platillo
    if 'q' in request.GET:
        query = request.GET.get('q')
        print("Query:", query)  # Verifica el valor de query en la consola
        try:
            # Busca un platillo cuyo nombre coincida exactamente con query
            Platillo_seleccionado = Menu.objects.get(Nombre__iexact=query)
        except Menu.DoesNotExist:
            pass

    print("platillo_seleccionado: ", Platillo_seleccionado)
    return render(request, 'Menu/resultados_busqueda.html', {'platillo_seleccionado': Platillo_seleccionado})



def load_menu(request):
    if request.method == 'POST':
        formulario = Form_Comments(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/')
    else:
        formulario = Form_Comments()
    return render(request, 'Menu/upload_menu.html', {'formulario': formulario})

def base(request):
    menu = Menu.objects.all()
    return render(request, 'Menu/base_menu.html',{'Menu': menu})


def show_administrador(request):
    # Obtén todas las Platillos guardadas
    platillos = Menu.objects.all()
    
    # Verifica si se está realizando una búsqueda
    if 'q' in request.GET:
        query = request.GET.get('q')
        try:
            platillo = Menu.objects.get(Nombre__iexact=query)
            resultados = [{'Platillo': platillo.Nombre, 'Categoria': platillo.categoria}]
            return JsonResponse(resultados, safe=False)
        except Menu.DoesNotExist:
            # Handle the case when no matching Menu object is found
            resultados = [{'Platillo': 'No se encontraron resultados'}]
            return JsonResponse(resultados, safe=False)
    
    # Si no hay búsqueda, renderiza la plantilla con todas las platillos
    return render(request, 'Menu/administrador.html', {'platillos': platillos})

def show_cocina(request):
    # Obtén todas las Platillos guardadas
    platillos = Menu.objects.all()
    
    # Verifica si se está realizando una búsqueda
    if 'q' in request.GET:
        query = request.GET.get('q')
        try:
            platillo = Menu.objects.get(Nombre__iexact=query)
            resultados = [{'Platillo': platillo.Nombre, 'Categoria': platillo.categoria}]
            return JsonResponse(resultados, safe=False)
        except Menu.DoesNotExist:
            # Handle the case when no matching Menu object is found
            resultados = [{'Platillo': 'No se encontraron resultados'}]
            return JsonResponse(resultados, safe=False)
    
    # Si no hay búsqueda, renderiza la plantilla con todas las platillos
    return render(request, 'Menu/cocina.html', {'platillos': platillos})

def show_mesero(request):
    mesero = Mesero.objects.all()
    return render(request, 'Menu/mesero.html',{'Mesero': mesero})

def show_cliente(request):
    # Obtén todas las Platillos guardadas
    platillos = Menu.objects.all()
    
    # Verifica si se está realizando una búsqueda
    if 'q' in request.GET:
        query = request.GET.get('q')
        try:
            platillo = Menu.objects.get(Nombre__iexact=query)
            resultados = [{'Platillo': platillo.Nombre, 'Categoria': platillo.categoria}]
            return JsonResponse(resultados, safe=False)
        except Menu.DoesNotExist:
            # Handle the case when no matching Menu object is found
            resultados = [{'Platillo': 'No se encontraron resultados'}]
            return JsonResponse(resultados, safe=False)
    
    # Si no hay búsqueda, renderiza la plantilla con todas las platillos
    return render(request, 'Menu/cliente.html', {'platillos': platillos})

from django.shortcuts import render, get_object_or_404, redirect

def modificar_menu(request, id):
    # lógica para modificar el menú
    menu_item = get_object_or_404(Menu, id=id)
    if request.method == "POST":
        # Procesar el formulario
        pass
    else:
        # Renderizar el formulario
        pass
    return render(request, 'modificar_menu.html', {'menu_item': menu_item})

def eliminar_menu(request, id):
    # lógica para eliminar el menú
    menu_item = get_object_or_404(Menu, id=id)
    if request.method == "POST":
        menu_item.delete()
        return redirect('nombre_de_tu_vista_principal')
    return render(request, 'eliminar_menu.html', {'menu_item': menu_item})

def orden_view(request):
    return render(request, 'Menu/orden.html')