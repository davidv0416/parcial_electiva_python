from calendar import weekday
from django.http import HttpResponse
from django.shortcuts import render
from ast import Return
from datetime import datetime, date, time


def formulario(request):
    return render(request,'paginas/formulario.html')

def calcular(request):
    if(request.POST):
        recibedatos = request.POST.dict()
        nombre = recibedatos.get("nombre")
        año = int(recibedatos.get("año"))
        mes = int(recibedatos.get("mes"))
        dia = int(recibedatos.get("dia"))
        
        
        tiempo = datetime.now()
        año1 = int(tiempo.year) 
        mes1 = int(tiempo.month)
        dia1 = int(tiempo.day)
        
        
        if (mes > mes1):
            edad_años = año1 - año - 1
        else: edad_años = año1 - año
        
        
       
        """ 
        if (dia == 1):
            dia_nacimiento = "Lunes"
        elif (dia == 2):
            dia_nacimiento = "Martes"
        elif (dia == 3):
            dia_nacimiento = "Miércoles"
        elif (dia == 4):
            dia_nacimiento = "Jueves"
        elif (dia == 5):
            dia_nacimiento = "Viernes"
        elif (dia == 6):
            dia_nacimiento = "Sábado"
        elif (dia == 7):
            dia_nacimiento = "Domingo"
        """
        
    return HttpResponse ("Tu edad es de %s años" %(edad_años,))

