from django.shortcuts import render
from Menu.models import Producto,Categorias
# Create your views here.
def Menu(request):
    allproducto= Producto.objects.all()
    categorias=Categorias.objects.all()
    cantidad_productos=allproducto.count
    return render(request,'menu.html',{"productos":allproducto,"categorias":categorias,"cantidad_productos":cantidad_productos})

def MenuxCategorias(request,categoria):
    cat=Categorias.objects.get(nombre=categoria)
    productos=Producto.objects.filter(categoria=cat.id)
    categorias=Categorias.objects.all()
    cantidad_productos=productos.count
    return render(request,'menu.html',{"productos":productos,"categorias":categorias,"cantidad_productos":cantidad_productos})
