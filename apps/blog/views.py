from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.mail import send_mail
from .forms import Associado
from .forms import Inscricao
from django.conf import settings
from .models import Home
from .models import Quemsomos
from .models import Card
from .models import Servico
from .models import Beneficios

# Create your views here. nossos_serviços.html

def post_list(request):  
    quemsomos = Quemsomos.objects.get(id = 1)
    home = Home.objects.get(id = 1)
    cards = Card.objects.all()
    beneficios = Beneficios.objects.get(id = 1)

    context = {}
    if request.method == 'POST':

            form = Associado(request.POST)
            if form.is_valid():
                context['is_valid'] = True
                form.send_mail()
                form = Associado()

    else:
        form = Associado()


    context['home'] = home
    context['form'] = form
    context['cards'] = cards
    context['beneficios'] = beneficios
    context['quemsomos'] = quemsomos

    return render(request, 'index.html', context)

def voltar(request, slug):  
    quemsomos = Quemsomos.objects.get(id = 1)
    home = Home.objects.get(id = 1)
    cards = Card.objects.all()
    beneficios = Beneficios.objects.get(id = 1)

    context = {}
    if request.method == 'POST':
        form = Associado(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail()
            form = Associado()

    else:
        form = Associado()

    context['home'] = home
    context['form'] = form
    context['cards'] = cards
    context['beneficios'] = beneficios
    context['quemsomos'] = quemsomos

    return render(request, 'index2.html', context)

def natal(request):
    return render(request,'conheça_natal.html',)

def voltar_natal(request, slug):
    return render(request,'conheça_natal.html',)

def servicos(request):
    servicos = Servico.objects.get(id = 1)
    return render(request,'nossos_serviços.html',{'servicos': servicos,})

def voltar_servicos(request, slug):
    servicos = Servico.objects.get(id = 1)
    return render(request,'nossos_serviços.html',{'servicos': servicos,})

def evento(request, slug):
    cards = get_object_or_404(Card, slug=slug)
    return render(request,'eventos.html',{'cards': cards,})

def inscricao(request, slug):
    cards = get_object_or_404(Card, slug=slug)
    context = {}
    if request.method == 'POST':
        form = Inscricao(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(cards)
            form = Inscricao()

    else:
        form = Inscricao()

    context['form'] = form
    context['cards'] = cards

    return render(request, 'inscrição.html', context)


