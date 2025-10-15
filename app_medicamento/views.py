
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicamento

# Listar estudiantes
def index(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'listar_medicamentos.html', {'medicamentos': medicamentos})

# Ver estudiante (opcional, puedes usarlo si quieres detalle)
def ver_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, id=id)
    return render(request, 'ver_medicamento.html', {'medicamento': medicamento})

# Agregar estudiante
def agregar_medicamento(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        funcion = request.POST['funcion']
        presentacion = request.POST['presentacion']
        precio = request.POST['precio']
        stock = request.POST['stock']
        Medicamento.objects.create(nombre=nombre, funcion=funcion, presentacion=presentacion, precio=precio, stock=stock)
        return redirect('inicio')
    return render(request, 'agregar_medicamentos.html')

# Editar estudiante
def editar_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, id=id)
    if request.method == 'POST':
        medicamento.nombre = request.POST['nombre']
        medicamento.funcion = request.POST['funcion']
        medicamento.presentacion = request.POST['presentacion']
        medicamento.precio = request.POST['precio']
        medicamento.stock = request.POST['stock']
        medicamento.save()
        return redirect('inicio')
    return render(request, 'editar_medicamentos.html', {'medicamento': medicamento})

# Borrar estudiante
def borrar_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, id=id)
    if request.method == 'POST':
        medicamento.delete()
        return redirect('inicio')
    return render(request, 'borrar_medicamentos.html', {'medicamento': medicamento})
