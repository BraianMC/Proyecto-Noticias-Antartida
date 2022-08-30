from django import forms
from App_RDNA.models import Usuario,Pais,Categoria,Fuente_Informacion,Contenido_Procesado
from django.db.models import fields


class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=[
            'nombre',
            'contraseña',
        ]


class Fuente_InformacionForm(forms.ModelForm):
    class Meta:
        model=Fuente_Informacion
        fields=[
            'nombre',
            'URL',
            'tipo',
             
        ]

class PaisForm(forms.ModelForm):
    class Meta:
        model=Pais
        fields=[
            'nombre',
            'idioma',
           
        ]




class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields=[
            'concepto',
            
        ]
'''
class Contenido_ProcesadoForm(forms.ModelForm):
    class Meta:
       model=Contenido_Procesado
       fields=[
            'titulo',
            'fecha_creacion',
            'contenido',
            'anotacion',
            'idAdjunto',
            'idContenido_original',
        ]

'''