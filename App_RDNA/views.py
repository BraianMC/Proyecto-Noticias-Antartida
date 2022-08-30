from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from . import models
from App_RDNA.models import Usuario,Pais,Categoria,Fuente_Informacion,Contenido_Procesado
from App_RDNA.forms import UsuarioForm,Fuente_InformacionForm,PaisForm,CategoriaForm
from django.views.generic import ListView,TemplateView,CreateView,UpdateView,DeleteView,DetailView



class InicioView(ListView):
    template_name=''
    queryset=Categoria.objects.all()
    context_object_name="categorias"
   


class PanelAdminView(TemplateView):
    template_name=''

class ListarUsuarios(ListView):
    queryset=Usuario.objects.all()
    context_object_name="usuarios"
    template_name=""

class ListarPaises(ListView):
    queryset=Pais.objects.all()
    context_object_name="paises"
    template_name=""

class ListarCategorias(ListView):
    queryset=Categoria.objects.all()
    context_object_name="categorias"
    template_name=""

class CrearCategoria(CreateView):
    model=Categoria
    form_class=CategoriaForm
    queryset=Categoria.objects.all()
    template_name=""
    success_url=reverse_lazy('')
    
class CrearPais(CreateView):
    model=Pais
    form_class=PaisForm
    queryset=Pais.objects.all()
    template_name=""
    success_url=reverse_lazy('')

class CrearFuente(CreateView):
    model=Fuente_Informacion
    form_class=Fuente_InformacionForm
    queryset=Fuente_Informacion.objects.all()
    template_name=""
    success_url=reverse_lazy('')
    

class CrearUsuario(CreateView):
    model=Usuario
    form_class=UsuarioForm
    queryset=Usuario.objects.all()
    template_name=""
    success_url=reverse_lazy('')


class ListarFuentes(ListView):
    queryset=Fuente_Informacion.objects.all()
    context_object_name="fuentes"
    template_name=""

class ActualizarCategoria(UpdateView):
    model=Categoria
    form_class=CategoriaForm
    template_name=''
    success_url=reverse_lazy('')

class ActualizarFuente(UpdateView):
    model=Fuente_Informacion
    form_class=Fuente_InformacionForm
    template_name=''
    success_url=reverse_lazy('')

class ActualizarPais(UpdateView):
    model=Pais
    form_class=PaisForm
    template_name=''
    success_url=reverse_lazy('')

class ActualizarUsuario(UpdateView):
    model=Usuario
    form_class=UsuarioForm
    template_name=''
    success_url=reverse_lazy('')

class EliminarCategoria(DeleteView):
    model=Categoria
    form_class=CategoriaForm
    template_name=''
    success_url=reverse_lazy('')

class EliminarPais(DeleteView):
    model=Pais
    form_class=PaisForm
    template_name=''
    success_url=reverse_lazy('')

class EliminarFuente(DeleteView):
    model=Fuente_Informacion
    form_class=Fuente_InformacionForm
    template_name=''
    success_url=reverse_lazy('')
    

class ListarContenido(ListView):
    queryset=Contenido_Procesado.objects.all()
    context_object_name="contenidos"
    template_name=""



def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = models.Contenido_Procesado(
            titulo = fileTitle,
            contenido = uploadedFile
        )
        document.save()

    documents = models.Contenido_Procesado.objects.all()

    return render(request, "", context = {
        "files": documents
    }) 