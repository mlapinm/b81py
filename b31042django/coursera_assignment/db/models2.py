# models2.py
from django.db import models

class Blog2(models.Model):
    name = models.CharField(max_length=100) 
    tagline = models.TextField()

class Author2(models.Model):
    name = models.CharField(max_length=200) 
    email = models.EmailField()

class Entry2(models.Model):
    blog = models.ForeignKey(Blog2, on_delete=models.CASCADE) 
    headline = models.CharField(max_length=255, blank=True, null=True, default=None)
    authors = models.ManyToManyField(Author2)
    
