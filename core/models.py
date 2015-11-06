from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    telefone = models.CharField(u'Celular', max_length=14, help_text='(99)99999-9999')
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

class ProdutoProfiles(models.Model):
    CATEGORIA_CHOICES = (
        ('RF','Roupas Femininas'),
        ('RM','Roupas Masculinas'),
        ('MI', 'Moda Intima'),
        ('IN', 'Moda Infantil'),
        )

    nome=models.CharField(u'nome',max_length=50)
    referencia=models.CharField( u'Referencia',max_length=50)
    quantidade=models.CharField(u'quantidade',max_length=5)
    categoria = models.CharField(max_length=2, choices=CATEGORIA_CHOICES)
    preco = models.CharField(u'preco',max_length = 10, help_text='R$ 0,00')

