from django.db import models

class User(models.Model):
    username = models.CharField('Username', max_length=100)
    password = models.CharField('Password', max_length=100)
    email = models.CharField('Email', max_length=50)

