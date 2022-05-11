from django.shortcuts import render
from .models import Inventario

def index(request):
    list = Inventario.objects.order_by('-tombo')[:5]
    context = {'list': list}
    return render(request, 'AplicativoInventario/index.html', context)