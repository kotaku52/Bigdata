from django.db import models

# Create your models here.
class classfi(models.Model):
    input_value = models.CharField(max_length=100)
    result = models.CharField(max_length=20)
