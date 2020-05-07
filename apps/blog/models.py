from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
# preco    = models.DecimalField(max_digits = 9, decimal_places = 2)

class Post(models.Model):
    titulo   = models.CharField(max_length = 30, blank= False, verbose_name ='de um titulo para a etiqueta')
    descricao= models.TextField(verbose_name = 'descrição de quem somos', blank= False)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Quem Somos'
        verbose_name_plural = 'Quem Somos'

class Missao(models.Model):
    titulo   = models.CharField(max_length = 30, blank= False, verbose_name ='de um titulo para a etiqueta')
    descricao= models.TextField(verbose_name = 'descrição de quem somos', blank= False)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Missão'
        verbose_name_plural = 'Missão'

class Visao(models.Model):
    titulo   = models.CharField(max_length = 30, blank= False, verbose_name ='de um titulo para a etiqueta')
    descricao= models.TextField(verbose_name = 'descrição de quem somos', blank= False)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Visão'
        verbose_name_plural = 'Visão'

class Valores(models.Model):
    titulo   = models.CharField(max_length = 30, blank= False, verbose_name ='de um titulo para a etiqueta')
    descricao= models.TextField(verbose_name = 'descrição de quem somos', blank= False)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Valores'
        verbose_name_plural = 'Valores'

class Card(models.Model):
    titulo   = models.CharField(max_length = 30, blank= False, verbose_name ='de um titulo para a etiqueta')
    descricao= models.TextField(max_length= 50, blank= False, verbose_name = 'descrição do evento')
   
    imagem   = models.ImageField(
        upload_to= 'eventos/',
        null= True,
        blank= False,
        verbose_name= 'imagem do evento',
    )


    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'
        
class Servico(models.Model):
    titulo   = models.CharField(max_length = 30, blank= False, verbose_name ='de um titulo para a etiqueta')
    descricao= models.TextField(verbose_name = 'descrição de quem somos', blank= False)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        
class Beneficios(models.Model):
    titulo   = models.CharField(max_length = 30, blank= False, verbose_name ='de um titulo para a etiqueta')
    descricao= models.TextField(verbose_name = 'descrição de quem somos', blank= False)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Beneficio'
        verbose_name_plural = 'Beneficios'

class Contatos(models.Model):
    titulo   = models.CharField(max_length = 30, blank= False, verbose_name ='de um titulo para a etiqueta')
    instagram   = models.CharField(max_length = 30, blank= False, verbose_name ='Instagram')
    facebook  = models.CharField(max_length = 30, blank= False, verbose_name ='Facebook')
    email   = models.CharField(max_length = 30, blank= False, verbose_name ='E-mail')
    telefone   = models.CharField(max_length = 30, blank= False, verbose_name ='Telefone')
    endereco   = models.TextField(verbose_name = 'Endereço', blank= False)
    twitter   = models.CharField(max_length = 30, blank= False, verbose_name ='Twitter')
    

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        
