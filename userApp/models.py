from django.db import models

# Create your models here.
class User_registraton(models.Model):
    Name = models.CharField(max_length=200,null=False,blank=False)
    Email = models.EmailField(max_length=100,null=False,blank=False)
    Role = models.CharField(max_length=50,null=False,blank=False)
    FromTime = models.IntegerField()
    ToTime = models.IntegerField()
