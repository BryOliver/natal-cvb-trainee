from django.contrib import admin
from .models import Home
from .models import Quemsomos
from .models import Card
from .models import Servico
from .models import Beneficios

admin.site.register(Home)
admin.site.register(Quemsomos)
admin.site.register(Card)
admin.site.register(Servico)
admin.site.register(Beneficios)
# Register your models here.
