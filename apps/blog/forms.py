from django import forms
from django.core.mail import send_mail
from django.conf import settings

from core.mail import send_mail_template

class SejaAssociado(forms.Form):
    nome = forms.CharField(label='Nome completo', max_length=100, widget=forms.TextInput(attrs={'class': 'form_control',}))
    empresa = forms.CharField(label='Empresa', max_length=100, widget=forms.TextInput(attrs={'class': 'form_control',}))
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'class': 'form_control',}))
    telefone = forms.CharField(label='Telefone para contato', max_length=100, widget=forms.TextInput(attrs={'class': 'form_control',}))
    descricao = forms.CharField(label='Descrição da empresa', max_length=100, widget=forms.TextInput(attrs={'class': 'form_control',}))

    def send_mail(self):
        subject = 'Contato Associado',
        context = {
            'nome': self.cleaned_data['nome'],
            'empresa': self.cleaned_data['empresa'],
            'email': self.cleaned_data['email'],
            'telefone': self.cleaned_data['telefone'],
            'descricao': self.cleaned_data['descricao'],
        }   

        template_name = 'associado.html'
        send_mail_template(subject, template_name, context, [settings.CONTACT_EMAIL])


class Inscrever(forms.Form):
    nome = forms.CharField(label='Nome completo', max_length=100, widget=forms.TextInput(attrs={'class': 'form_control',}))
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'class': 'form_control',}))
    telefone = forms.CharField(label='Telefone para contato', max_length=100, widget=forms.TextInput(attrs={'class': 'form_control',}))

    def send_mail(self):
        subject = 'Contato Associado',
        context = {
            'nome': self.cleaned_data['nome'],
            'email': self.cleaned_data['email'],
            'telefone': self.cleaned_data['telefone'],
        }   

        template_name = 'inscrito.html'
        send_mail_template(subject, template_name, context, [settings.CONTACT_EMAIL])