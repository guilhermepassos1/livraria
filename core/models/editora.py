from django.db import models 

class Editora(models.Model):
    nome = models.CharField(max_lengh=100)
    url = models.URLField(max_lengh=100)