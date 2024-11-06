from django.db import models
#3. Definir o Modelo de Cadastro
#Depois de sair de "sistema/settings.py"
class Cliente (models.Model): #models.Models é a representação dos dados
    nome = models.CharField (max_length=100) # Cada campo criado são campos que são adicionados no modelo
    email = models.EmailField (unique=True)
    telefone = models.CharField(max_length=30)
    endereco = models.TextField()
    
    def __str__(self):
        return self.nome
# Create your models here.
