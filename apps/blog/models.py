from django.db import models
from django.conf import settings
from django.utils import timezone


# from django.core.urlresolvers import reverse
# Create your models here.

class Home(models.Model):
    titulo   = models.CharField(null = True, max_length = 30, blank= False, verbose_name ='Titulo para a exibição')
    
    imagem   = models.ImageField(
        upload_to= 'home/',
        null= True,
        blank= False,
        verbose_name= 'Imagem de fundo do banner inicial',
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Banner inicial'
        verbose_name_plural = 'Banner inicial'

class Quemsomos(models.Model):
    titulo   = models.CharField(null = True, max_length = 30, blank= False, verbose_name ='Titulo para a exibição')
    descricao= models.TextField(null = True, verbose_name = 'Descrição de quem somos', blank= False)
    missao   = models.TextField(null = True, verbose_name = 'Missão', blank= False)
    visao    = models.TextField(null = True, verbose_name = 'Visão', blank= False)
    valores  = models.TextField(null = True, verbose_name = 'Valores', blank= False)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Quem Somos'
        verbose_name_plural = 'Quem Somos'

class Card(models.Model):
    titulo   = models.CharField(null = True, max_length = 30, blank= False, verbose_name ='Titulo para a exibição')
    descricao= models.TextField(null = True, max_length= 100, blank= False, verbose_name = 'Descrição do evento')
   
    imagem   = models.ImageField(
        upload_to= 'eventos/',
        null= True,
        blank= False,
        verbose_name= 'Imagem do evento',
    )

    evento   = models.TextField(null= True, blank= False, verbose_name = 'Descrição na página do evento')
    local   = models.CharField(max_length= 100, null= True, blank= False, verbose_name = 'Local do evento')
    slug     = models.SlugField(null= True, verbose_name='Atalho na URL')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Data/Hora do evento')

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.titulo

    
    def get_absolute_url(self): 
        from django.urls import reverse
        return reverse('evento', args=[self.slug])
    
    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'
        
class Servico(models.Model):
    titulo   = models.CharField(null = True, max_length = 30, blank= False, verbose_name ='Titulo para a exibição')
    eventoshoteis= models.TextField(null = True, verbose_name = 'Eventos e hotéis', blank= False)
    alimentosebebidas= models.TextField(null = True, verbose_name = 'Alimentos e bebidas', blank= False)
    transporte= models.TextField(null = True, verbose_name = 'Transporte', blank= False)
    outrosservicos= models.TextField(null = True, verbose_name = 'Outros serviços', blank= False)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        
class Beneficios(models.Model):
    titulo   = models.CharField(null = True, max_length = 30, blank= False, verbose_name ='Titulo para a exibição')
    descricao= models.TextField(null = True, verbose_name = 'Lista de benefícios', blank= False)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Benefício'
        verbose_name_plural = 'Benefícios'

