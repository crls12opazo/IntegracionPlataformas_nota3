from django.db import models
class Atencion(models.Model):
    id_atencion = models.AutoField(primary_key=True)
    rut_medico = models.CharField(max_length=12, unique=True)
    nombre_medico = models.CharField(max_length=40)
    rut_paciente = models.CharField(max_length=12)
    nombre_paciente = models.CharField(max_length=40)
    fecha_atencion = models.DateField()
    consulta = models.CharField(max_length=200)
    procedimiento = models.CharField(max_length=200)
    receta = models.CharField(max_length=200)    
    class Meta:
        db_table = 'atenciones'