from django import forms
from django.core.mail import send_mail
from django.conf import settings
from core.mail import send_mail_template
from django.core.validators import RegexValidator


class Associado(forms.Form):

    nome = forms.CharField(label='Nome completo:', max_length=100, widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': '  ex: Fulano de Tal'}))
    empresa = forms.CharField(label='Empresa:', max_length=100, widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': '  ex: Empresa X'}))
    email = forms.EmailField(label='E-mail:', widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': '  ex: fulanodetal@gmail.com'}))
    telefone = forms.CharField(
        validators=[RegexValidator(r'^[0-9,-,(,),]+$', 'Enter a valid extension.')],
        required=False,
        label='Telefone (Apenas números)', max_length=100, widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': '  ex: (84) 9 9999-9999'}))
    descricao = forms.CharField(label='Descrição da empresa:', max_length=100, widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': '  ex: empresa de serviços web'}))


    def send_mail(self,):
        subject = 'Pedido de Associamento' 
        context = {
            'nome': self.cleaned_data['nome'],
            'empresa': self.cleaned_data['empresa'],
            'email': self.cleaned_data['email'],
            'telefone': self.cleaned_data['telefone'],
            'descricao': self.cleaned_data['descricao'],
        }
        template_name = 'associado.html'
        send_mail_template(subject,template_name, context, [settings.CONTACT_EMAIL])

class Inscricao(forms.Form):

    nome = forms.CharField(label='Nome completo', max_length=100, widget=forms.TextInput(attrs={'class': 'text_bar', 'placeholder': '  ex: Fulano de Tal'}))
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'class': 'text_bar', 'placeholder': '  ex: fulanodetal@gmail.com'}))
    telefone = forms.CharField(label='Telefone', max_length=100, widget=forms.TextInput(attrs={'class': 'text_bar', 'placeholder': '  ex: (84) 9 9999-9999'}))


    def send_mail(self, cards):
        subject = '[%s] | Inscrição' % cards
        context = {
            'nome': self.cleaned_data['nome'],
            'email': self.cleaned_data['email'],
            'telefone': self.cleaned_data['telefone'],
            
        }
        template_name = 'inscrito.html'
        send_mail_template(subject,template_name, context, [settings.CONTACT_EMAIL])