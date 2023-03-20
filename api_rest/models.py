from django.db import models


class User(models.Model):                                                                           ## Herda models DjangoDB

    user_nickname = models.CharField(primary_key= True, max_length= 100, default= '')
    user_nome = models.CharField(max_length=150,default='')                                           ##Campos da tabela do BD
    user_email = models.EmailField(default='')
    user_age = models.IntegerField(default=0)

    def __str__(self):
        return f'Nickname: {self.user_nickname} | E-mail: {self.user_email}'                            ## Printar essa classe dessa função
    
