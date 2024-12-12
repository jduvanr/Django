from django.shortcuts import render
from django.http import HttpResponse
from . models import Clientes

def mclientes(request):
    obj=Clientes.objects.all().values("nombre")
    response_var=f"<h2>hola </h2>"
    for i in obj:
        response_var +=f"{i}"

    return HttpResponse(response_var)   



# Create your views here.
