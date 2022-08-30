"""Noticias_antartida URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path
from App_RDNA.views import InicioView,PanelAdminView,ListarCategorias,ListarFuentes,ListarPaises,ListarUsuarios,CrearCategoria,CrearPais,CrearFuente,CrearUsuario,ActualizarCategoria,ActualizarFuente,ActualizarPais,ActualizarUsuario,EliminarCategoria,EliminarPais,EliminarFuente,ListarContenido,uploadFile
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('inicio/', InicioView.as_view(),name='Principal'), 
    path('Administracion/', PanelAdminView.as_view(),name='PanelAdmin'), 
    path('ListadoUsuarios/', ListarUsuarios.as_view(),name='Usuario_listar'),
    path('ListadoCategorias/', ListarCategorias.as_view(),name='Categoria_listar'),
    path('ListadoFuentes/', ListarFuentes.as_view(),name='Fuente_listar'),
    path('ListadoPais/', ListarPaises.as_view(),name='Pais_listar'),
    path('CrearCategoria/', CrearCategoria.as_view(),name='Categoria_crear'),
    path('CrearPais/', CrearPais.as_view(),name='Pais_crear'),
    path('CrearFuente/', CrearFuente.as_view(),name='Fuente_crear'),
    path('CrearUsuario/', CrearUsuario.as_view(),name='Usuario_crear'),
    path('ActualizarUsuario/(P<pk>\d+)/',ActualizarUsuario.as_view(),name='Usuario_actualizar'),
    path('ActualizarPais/(P<pk>\d+)/',ActualizarPais.as_view(),name='Pais_actualizar'),
    path('ActualizarFuente/(P<pk>\d+)/',ActualizarFuente.as_view(),name='Fuente_actualizar'),
    path('ActualizarCategoria/(P<pk>\d+)/',ActualizarCategoria.as_view(),name='Categoria_actualizar'),
    path('EliminarCategoria/(P<pk>\d+)/', EliminarCategoria.as_view(),name='Categoria_eliminar'),
    path('EliminarPais/(P<pk>\d+)/', EliminarPais.as_view(),name='Pais_eliminar'),
    path('EliminarFuente/(P<pk>\d+)/', EliminarFuente.as_view(),name='Fuente_eliminar'),
    path('ListarContenido/', ListarContenido.as_view(),name='Contenido_listar'),
    path('CrearContenido/', uploadFile,name='uploadFile'),
]
   
