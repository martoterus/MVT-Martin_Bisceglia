from django.http import HttpResponse
from django.shortcuts import render
from AppMVT.models import familiares

# Create your views here.

def familia(self,nombre, edad, fecha_nac, lugar_nac):

    fam = familiares(nombre=nombre, edad=edad, fecha_nac=fecha_nac, lugar_nac=lugar_nac)
    fam.save()
    
    datos = f"Nombre: {fam.nombre}, edad: {fam.edad} años, fecha_nac: {fam.fecha_nac}, lugar_nac: {fam.lugar_nac}"
    return HttpResponse(datos)


def listafamiliares(self):
    
    lista = familiares.objects.all()
    return render(self, "Listafamiliar.html", {"Familiares": lista})