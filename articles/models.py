from re import M, T
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Articles(models.Model):
    
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)