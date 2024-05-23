from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from .models import Menu, Mesa, Orden, Categoria_platillo, Mesero, Perfil
from .forms import Form_Comments, RegistroForm  # Importa el formulario de registro

# Función para verificar el tipo de usuario
def verificar_tipo_usuario(user, tipo_esperado):
    if user.perfil.tipo_usuario != tipo_esperado:
        raise PermissionDenied

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

@login_required
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

@login_required
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

@login_required
def show_mesero(request):
    meseros = Mesero.objects.all()
    ordenes = Orden.objects.all()
    mesa = Mesa.objects.all()
    contexto = {
        'Mesero': meseros,
        'Orden': ordenes,
        'Mesa':mesa,
    }
    return render(request, 'Menu/Mesero.html', contexto)

@login_required
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

@login_required
def show_orden(request):
    # Obtén todas las Platillos guardadas
    platillos = Menu.objects.all()
    
    # Verifica si se está realizando una búsqueda
    if 'q' in request.GET:
        query = request.GET.get('q')
        try:
            platillo = Menu.objects.get(Nombre__iexact=query)
            resultados = [{'Platillo': platillo.Nombre, 'Precio': platillo.Precio}]
            return JsonResponse(resultados, safe=False)
        except Menu.DoesNotExist:
            # Handle the case when no matching Menu object is found
            resultados = [{'Platillo': 'No se encontraron resultados'}]
            return JsonResponse(resultados, safe=False)
    
    # Si no hay búsqueda, renderiza la plantilla con todas las platillos
    return render(request, 'Menu/orden.html', {'platillos': platillos})


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            Perfil.objects.create(user=user, tipo_usuario='cliente')  # Ajusta según tu lógica
            login(request, user)
            return redirect('/')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.perfil.tipo_usuario == 'administrador':
                    return redirect('../administrador')
                elif user.perfil.tipo_usuario == 'cliente':
                    return redirect('../cliente')
                elif user.perfil.tipo_usuario == 'mesero':
                    return redirect('../mesero')
                elif user.perfil.tipo_usuario == 'cocinero':
                    return redirect('../cocina')
                else:
                    return redirect('/login')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})