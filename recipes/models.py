from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name=models.CharField(max_length=65) #nome da categoria campo de texto com tamanho maximo de 65 caracteres
    

    def __str__(self): #metodo para retornar o nome da categoria como representacao em string
        return self.name #retorna o nome da categoria

    

# Create your models here.
class Recipe(models.Model):
    title=models.CharField(max_length=65) #titulo campo de texto com tamanho maximo de 65 caracteres
    description=models.CharField(max_length=165) #descricao campo de texto com tamanho maximo de 165 caracteres
    slug=models.SlugField(unique=True) #slug campo de texto para url amigavel
    preparation_time=models.FloatField() #tempo de preparo campo inteiro numero
    preparation_time_unit=models.CharField(max_length=65) #unidade de tempo campo de texto com tamanho maximo de 65 caracteres
    servings=models.IntegerField() #porcoes campo inteiro numero
    servings_unit=models.CharField(max_length=65) #unidade de porcoes campo de texto com tamanho maximo de 65 caracteres
    preparation_steps=models.TextField() #passos de preparo campo de texto longo    
    preparation_steps_is_html=models.BooleanField(default=False) #se os passos de preparo estao em html campo booleano verdadeiro ou falso
    ingredients_list=models.TextField() #lista de ingredientes campo de texto longo
    preparation_list_is_html=models.BooleanField(default=False) #se os passos de preparo estao em html campo booleano verdadeiro ou falso
    created_at=models.DateTimeField(auto_now_add=True) #data de criacao campo de data e hora
    updated_at=models.DateTimeField(auto_now=True) #data de atualizacao campo de data e hora
    is_published=models.BooleanField(default=False) #se a receita esta publicada campo booleano verdadeiro ou falso 
    cover=models.ImageField(upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='') #imagem de capa campo de imagem opcional, salvando na pasta recipes/covers/ano/mes/dia/
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=None) #categoria da receita campo de chave estrangeira para a categoria, pode ser nulo
    author=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) #autor da receita campo de chave estrangeira para o usuario, pode ser nulo

    def __str__(self):
        return self.title#metodo para retornar o titulo da receita como representacao em string