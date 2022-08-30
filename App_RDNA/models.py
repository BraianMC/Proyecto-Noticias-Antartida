from django.db import models
from django.db.models.expressions import OrderBy
from django.db.models.fields import BLANK_CHOICE_DASH
from django.db.models.fields.related import ForeignKey


class Usuario(models.Model):
    nombre = models.CharField(max_length = 30, null = False, blank = None)
    contraseña = models.CharField(max_length = 30, null = False, blank = None)

    def __str__(self):
        return self.nombre
     
  



class Admin(models.Model):
    idUsuario = models.ForeignKey(Usuario, null = False, blank = False, on_delete = models.CASCADE)



class Contenido_Original(models.Model):
    fecha_acceso = models.DateField(default = None, null = False, blank = None)
    contenido = models.TextField()



class Configuracion_Fuente_Informacion(models.Model):
    buscar_Titulo = models.CharField(max_length= 200,null = False, blank = None)
    buscar_Contenido = models.CharField(max_length = 200, null = False, blank = None)
    buscar_Imagenes = models.CharField(max_length = 200, null = False, blank = None)
    buscar_links = models.CharField(max_length = 200, null = False, blank = None)


class Pais(models.Model):
    nombre = models.CharField(max_length = 50, null = False, blank = None)
    idioma = models.CharField(max_length = 50, null = False, blank = None)
    

    def __str__(self):
        return self.nombre
    
    
class Fuente_Informacion(models.Model):
    nombre = models.CharField(max_length = 100, null = False, blank = None)
    URL = models.URLField(max_length = 200, null = False, blank = None)
    tipo = models.CharField(max_length = 30)
    fecha = models.DateField(default = datetime.date.today)
    idContenido_Original = models.ForeignKey( Contenido_Original, null = False, blank = False, on_delete = models.CASCADE)
    idConfiguracion = models.ForeignKey(Configuracion_Fuente_Informacion, null = False, blank = False, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre


    
   




class Contenido_Procesado(models.Model):
    titulo = models.CharField(max_length = 100, null = False, blank = None)
    fecha_Creacion = models.DateTimeField(auto_now = True)
    contenido = models.FileField(upload_to = "Uploaded Files/"  )
    anotacion = models.TextField(blank=True)
    idContenido_Original = models.ForeignKey(Contenido_Original, null = True, blank = True, on_delete = models.CASCADE)

    def __str__(self):
        return self.titulo
    
    


class Categoria(models.Model):
    concepto = models.CharField(max_length = 100, null = False, blank = None)
    contenidos_Procesados_Relacionados = models.ManyToManyField(Contenido_Procesado)

