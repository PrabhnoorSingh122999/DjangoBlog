# creating the category models here 

from django.db import models

class Health(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class Environment(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class Politics(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class Sports(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class Travel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()