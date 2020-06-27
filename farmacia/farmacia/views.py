from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
def index(request):
    if request.method == 'GET':
        hola="jpña"
        context={'hola':hola}
        return render(request,'farmacia/index.html',context)

def atencion(request):
    if request.method == 'GET':
        hola="jpña"
        context={'hola':hola}
    return render(request,'farmacia/atencion.html',context)

            

    