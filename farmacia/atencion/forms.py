from django import forms
from django.utils.timezone import datetime

class formularioAtencion(forms.Form):
    rutMedico=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type': 'text','id':'txtRutMedico', 'required oninput':'checkRut(this)','onblur':'validaRutTextBlur(this)' }))
    nombreMedico=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type': 'text','id':'txtNombreMedico'}))
    rutPaciente=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type': 'text','id':'txtRutPaciente' , 'required oninput':'checkRut(this)'}))
    nombrePaciente=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type': 'text','id':'txtNombrePaciente'}))
    hoy=datetime.today().date
    fecha=forms.DateField(widget = forms.TextInput(attrs={'class' : 'form-control', 'type' : 'date', 'min' :hoy,'id':'txtFecha'}))
    procedimiento=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','type': 'text','id':'txtProcedimiento','rows': 23, 'col':10}))
    consulta=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','type': 'text','id':'txtConsulta','rows': 5, 'col':10}))
    receta=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','type': 'text','id':'txtReceta','rows': 23, 'col':10}))

