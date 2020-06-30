from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from .forms import formularioAtencion
from .controllers import controllerAtencion
from dateutil.parser import parse
def atencion(request):
    if request.method == 'GET':
        form=formularioAtencion()
        hola = 'hola'
        context={'form':formularioAtencion,'message':hola}
        return render(request,'atencion.html',context)
    if request.method=='POST':
        form=formularioAtencion()
        rutMedico=request.POST['rutMedico']
        nombreMedico=request.POST['nombreMedico']
        rutPaciente=request.POST['rutPaciente']
        nombrePaciente=request.POST['nombrePaciente']
        fecha=parse(request.POST['fecha'])
        consulta=request.POST['consulta']
        procedimiento=request.POST['procedimiento']
        receta=request.POST['receta']
        message= controllerAtencion.SaveAtencion(rutMedico,nombreMedico,rutPaciente,nombrePaciente,fecha,consulta,procedimiento,receta)
        context={'form':formularioAtencion,'message':message}
        return render(request,'atencion.html',context)

            

    