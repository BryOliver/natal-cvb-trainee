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
]