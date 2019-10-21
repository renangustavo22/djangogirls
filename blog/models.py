from django.conf import settings
from django.db import models
from django.utils import timezone

class Post (models.Model):  #Define nosso Modelo (é um objeto) - models.Model significa que o Post é um modelo de Django, então o Django sabe que ele deve ser salvo no banco de dados

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #Link para outro modelo
    title = models.CharField(max_length=200) # definimos um texto com um número limitado de caracteres.
    text = models.TextField() # Campo de Texto
    created_date = models.DateTimeField(default=timezone.now) # Data e hora
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): #Funçao/método para publicar

        self.published_date = timezone.now()
        self.save()

    def __str__(self):

        return self.title



