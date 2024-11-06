#5. Configurar o Admin para o Modelo de Cliente
from django.contrib import admin
from .models import Cliente

admin.site.register (Cliente)

# Register your models here.
