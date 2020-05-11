from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import SejaAssociado
from .forms import Inscrever
from django.core.mail import send_mail
from django.conf import settings
from .models import Post
from .models import Cards
from .models import Cardsdois
from .models import Cardsum
from .models import Card
from .models import Servico
from .models import Beneficios
from .models import Missao
from .models import Visao
from .models import Valores
from .models import Contatos

# Create your views here. nossos_serviços.html

def post_list(request):

    if request.method == 'POST':
        form = SejaAssociado(request.POST)
        if form.is_valid():
            print(form.cleaned_data['nome'])
            print(form.cleaned_data['empresa'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['telefone'])
            print(form.cleaned_data['descricao'])
            form.send_mail()
            form = SejaAssociado()

    else:
        form = SejaAssociado()
    
    post = Post.objects.get(id = 1)
    cards = Cards.objects.all()
    cardsdois = Cardsdois.objects.get(id =1)
    cardsum = Cardsum.objects.all()
    card = Card.objects.get( id = 1)
    beneficios = Beneficios.objects.all()
    missao = Missao.objects.get(id = 1)
    visao = Visao.objects.get(id = 1)
    valores = Valores.objects.all()
    contatos = Contatos.objects.all()

    # try:
    #  cardsum = Cardsum.objects.get(id = 1)
    #  context = {'cardsum': cardsum,}
    # except Cardsum.DoesNotExist:
    #  cards = Cards.objects.all()


    context = {
        'cardsum': cardsum,
        'cardsdois': cardsdois,
        'cards': cards,
        'card': card,
        'beneficios': beneficios,
        'missao': missao,
        'visao': visao,
        'valores': valores,
        'post': post,
        'contatos': contatos,
        'form' : form,
    }
    return render(request, 'index.html', context)

def natal(request):
    conheca = Natal.objects.all()
    return render(request,'conheça_natal.html',{'conheca': conheca,})

def servicos(request):
    servicos = Servico.objects.all()
    return render(request,'nossos_serviços.html',{'servicos': servicos,})