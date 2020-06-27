from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
def atencion(request):
    if request.method == 'GET':
        hola="jpña"
        context={'hola':hola}
    return render(request,'atencion.html',context)

            

    