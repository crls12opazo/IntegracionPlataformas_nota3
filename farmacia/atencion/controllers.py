from .models import Atencion
class controllerAtencion:
    def SaveAtencion(rutMedico,nombreMedico,rutPaciente,nombrePaciente,fecha,consulta,procedimiento,receta):
        new_atencion=Atencion()
        new_atencion.rut_medico=rutMedico
        new_atencion.nombre_medico=nombreMedico
        new_atencion.rut_paciente=rutPaciente
        new_atencion.nombre_paciente=nombrePaciente
        new_atencion.fecha_atencion=fecha
        new_atencion.consulta=consulta
        new_atencion.procedimiento=procedimiento
        new_atencion.receta=receta
        
        try:
            new_atencion.save()
            
            message="Atencion Registrada"
            
        except Exception as inst:
            message="Ha ocurrido un error , no se han guardado los datos." + str(inst)
        return message
    
    



