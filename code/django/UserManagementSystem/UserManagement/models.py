from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    telephone = models.CharField(max_length=13)

class Circle(models.Model):
    name = models.CharField(max_length=30)
