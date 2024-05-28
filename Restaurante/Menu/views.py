from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from .models import Menu, Mesa, Orden, Categoria_platillo, Mesero, Perfil
from .forms import Form_Comments, RegistroForm, CustomAuthenticationForm   # Importa el formulario de registro
from django.views.decorators.csrf import csrf_exempt
import json
from urllib.parse import urlparse

# Función para verificar el tipo de usuario
def verificar_tipo_usuario(user, tipo_esperado):
    if user.perfil.tipo_usuario != tipo_esperado:
        raise PermissionDenied

# def show_food(request):
#     # Obtén todas las Platillos guardadas
#     platillos = Menu.objects.all()
    
#     # Verifica si se está realizando una búsqueda
#     if 'q' in request.GET:
#         query = request.GET.get('q')
#         try:
#             platillo = Menu.objects.get(Nombre__iexact=query)
#             resultados = [{'Platillo': platillo.Nombre, 'Categoria': platillo.categoria}]
#             return JsonResponse(resultados, safe=False)
#         except Menu.DoesNotExist:
#             # Handle the case when no matching Menu object is found
#             resultados = [{'Platillo': 'No se encontraron resultados'}]
#             return JsonResponse(resultados, safe=False)
    
#     # Si no hay búsqueda, renderiza la plantilla con todas las platillos
#     return render(request, 'Menu/index.html', {'platillos': platillos})

def index(request):
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
    return render(request, 'Menu/base.html', {'platillos': platillos})   


def busqueda(request):
    platillo_seleccionado = None  # Inicializa la variable en caso de que no se encuentre la canción
    if 'q' in request.GET:
        query = request.GET.get('q')
        print("Query:", query)  # Verifica el valor de query en la consola
        try:
            # Busca una canción cuyo título coincida exactamente con query
            platillo_seleccionado = Menu.objects.get(Nombre__iexact=query)
        except Menu.DoesNotExist:
            pass

    print("platillo_seleccionado: ", platillo_seleccionado)
    return render(request, 'Menu/resultados_busqueda.html', {'platillo_seleccionado': platillo_seleccionado})


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
    meseros = Mesero.objects.all()
    ordenes = Orden.objects.all()
    mesa = Mesa.objects.order_by('numero_mesa') 
    contexto = {
        'Mesero': meseros,
        'Orden': ordenes,
        'Mesa':mesa,
    }
    return render(request, 'Menu/cocina.html', contexto)

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
    # Obtén todas las canciones guardadas
    platillos = Menu.objects.all()
    
    # Verifica si se está realizando una búsqueda
    if 'q' in request.GET:
        query = request.GET.get('q')
        platillos = Menu.objects.filter(Nombre__icontains=query)
        resultados = [{'Nombre': platillo.Nombre, 'Descripcion': platillo.Descripcion} for platillo in platillos]
        return JsonResponse(resultados, safe=False)
    
    # Si no hay búsqueda, renderiza la plantilla con todas las canciones
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
    
    # Si no hay búsqueda ni se presiona el botón, renderiza la plantilla con todas las platillos
    return render(request, 'Menu/orden.html', {'platillos': platillos})

@login_required
def show_orden2(request):
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
    
    # Si no hay búsqueda ni se presiona el botón, renderiza la plantilla con todas las platillos
    return render(request, 'Menu/comprobante.html', {'platillos': platillos})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            num_mesa = form.cleaned_data.get('num_mesa')
            if num_mesa:
                Perfil.objects.create(user=user, tipo_usuario='cliente')
            else:
                Perfil.objects.create(user=user, tipo_usuario='cliente_mesa')
            login(request, user)
            return redirect('/')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Obtener el perfil del usuario
                perfil = Perfil.objects.get(user=user)
                # Redirigir según el tipo de usuario
                if perfil.tipo_usuario == 'administrador':
                    return redirect('/Menu/administrador')
                elif perfil.tipo_usuario == 'cliente':
                    return redirect('/')
                elif perfil.tipo_usuario == 'mesero':
                    return redirect('/Menu/mesero')
                elif perfil.tipo_usuario == 'cocinero':
                    return redirect('/Menu/cocina')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('/')

@login_required
def show_categoria(request, opcion):
    categorias = Categoria_platillo.objects.order_by('nombre_categoria')

    # Verifica si se está realizando una búsqueda
    if 'q' in request.GET:
        query = request.GET.get('q')
        try:
            categoria = Categoria_platillo.objects.get(nombre_categoria__iexact=query)
            platillos = Menu.objects.filter(categoria=categoria)
            resultados = [{'Platillo': platillo.Nombre, 'Precio': platillo.Precio} for platillo in platillos]
            return JsonResponse(resultados, safe=False)
        except Categoria_platillo.DoesNotExist:
            resultados = [{'Platillo': 'No se encontraron resultados'}]
            return JsonResponse(resultados, safe=False)

    if opcion == 1:
        categoria_tortas = get_object_or_404(Categoria_platillo, nombre_categoria__iexact='Tortas')
        platillos = Menu.objects.filter(categoria=categoria_tortas)
    elif opcion == 2:
        categoria_hamburguesas = get_object_or_404(Categoria_platillo, nombre_categoria__iexact='Hamburguesas')
        platillos = Menu.objects.filter(categoria=categoria_hamburguesas)
    elif opcion == 3:
        categoria_bebidas = get_object_or_404(Categoria_platillo, nombre_categoria__iexact='Bebidas')
        platillos = Menu.objects.filter(categoria=categoria_bebidas)
    elif opcion == 4:
        categoria_snaks = get_object_or_404(Categoria_platillo, nombre_categoria__iexact='Snaks')
        platillos = Menu.objects.filter(categoria=categoria_snaks)
    else:
        platillos = Menu.objects.none()  # Default to an empty queryset

    contexto = {
        'categorias': categorias,
        'opcion': opcion,
        'platillos': platillos,
    }

    return render(request, 'Menu/categoria.html', contexto)

#@csrf_exempt
#def crear_orden(request):
#    if request.method == "POST":
#        data = json.loads(request.body)
 #       id_mesero = data.get('id_mesero')
#        platillos = data.get('platillos')
 ##       comentario = data.get('comentario', '')
#
#        mesero = Mesero.objects.get(id=id_mesero)

 #       for platillo in platillos:
 #           menu_item = Menu.objects.get(id=platillo['id'])
#            cantidad = platillo['cantidad']
 #           Orden.objects.create(
  #              id_mesero=mesero,
   #             id_platillo=menu_item,
    #            cantidad=cantidad,
     #           comentario=comentario,
      #          estado=True
       #     )

        #return JsonResponse({'message': 'Orden creada exitosamente'})

 #   return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def insertar_valores_orden(request):
    if request.method == 'POST':
        # Aquí puedes definir los valores que deseas insertar en la tabla Orden
        # Por ejemplo:
        id_mesero = 1
        id_platillo = 4
        cantidad = 2
        comentario = "Comentario de prueba"
        
        # Inserta los valores en la tabla Orden
        orden = Orden.objects.create(id_mesero_id=id_mesero, id_platillo_id=id_platillo, cantidad=cantidad, comentario=comentario)
        
        return JsonResponse({'message': 'Valores insertados correctamente en la tabla Orden'})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    

def update_order_status(request):
    if request.method == 'POST':
        mesa_id = request.POST.get('mesa_id')
        try:
            mesa = Mesa.objects.get(id=mesa_id)
            orden = mesa.num_orden
            orden.estado = False
            orden.save()
            return JsonResponse({'success': True})
        except Mesa.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Mesa no encontrada'})
    return JsonResponse({'success': False, 'error': 'Método no permitido'})

@csrf_exempt
def crear_orden(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id_mesero = Mesero.objects.order_by('?').first()  # Selecciona aleatoriamente un mesero
        if not id_mesero:
            return JsonResponse({'error': 'No hay meseros disponibles'}, status=400)
        
        for platillo in data['platillos']:
            try:
                id_platillo = Menu.objects.get(Nombre=platillo['nombre'])  # Ajusta si 'Nombre' no es único
            except Menu.DoesNotExist:
                return JsonResponse({'error': f'Platillo {platillo["nombre"]} no encontrado'}, status=400)
            
            Orden.objects.create(
                id_mesero=id_mesero,
                id_platillo=id_platillo,
                cantidad=platillo.get('cantidad', 1),  # Suponiendo que la cantidad viene del frontend o por defecto es 1
                comentario=platillo.get('comentario', ''),  # Suponiendo que el comentario viene del frontend o por defecto es vacío
                estado=True  # O ajusta según la lógica de tu aplicación
            )
        return JsonResponse({'message': 'Orden creada exitosamente'})
    return JsonResponse({'error': 'Método no permitido'}, status=405)

