from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('conheça_natal.html', views.natal, name='natal'),
    path('nossos_serviços.html', views.servicos, name='servicos'),
    path('index.html', views.post_list, name='post_list'),
    
    path('eventos/<slug>/', views.evento, name='evento'),

    path('inscrição/<slug>/', views.inscricao, name='inscricao'),

    path('eventos/<slug>/index.html', views.voltar, name='voltar'),

    path('eventos/<slug>/nossos_serviços.html/', views.voltar_servicos, name='voltar_servicos'),

    path('eventos/<slug>/conheça_natal.html/', views.voltar_natal, name='voltar_natal'),
]