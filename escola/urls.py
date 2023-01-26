"""escola URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from django.conf.urls import include
from rest_framework import routers
from aluno.api.viewsets import AlunoViewSet
from disciplina.api.viewsets import DisciplinaViewSet
from estagio.api.viewsets import EstagioViewSet
from matricula.api.viewsets import MatriculaViewSet
from professor.api.viewsets import ProfessorViewSet

router = routers.DefaultRouter()
router.register(r'ListaAluno', AlunoViewSet, basename='ListaAluno')
router.register(r'ListaDisciplina', DisciplinaViewSet, basename='ListaDisciplina')
router.register(r'ListaEstagio', EstagioViewSet, basename='ListaEstagio')
router.register(r'ListaMatricula', MatriculaViewSet, basename='ListaMatricula')
router.register(r'ListaProfessor', ProfessorViewSet, basename='ListaProfessor')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),

]
