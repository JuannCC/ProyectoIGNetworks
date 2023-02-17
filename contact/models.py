from datetime import datetime
from email.policy import default
from django.db import models
from datetime import date
from django import forms
# Create your models here.

class Contact(models.Model):

    name= models.CharField(max_length=50, blank=False, null=False)
    clave=  models.BooleanField(default=False,help_text="Clikear si es cliente clave", verbose_name="Cliente clave?")
    cronico=  models.BooleanField(default=False,help_text="Clikear si es cliente cronico", verbose_name="Es cronico?")
    visibilidad=  models.BooleanField(default=False,help_text="Clikear si es el cliente tiene visibilidad", verbose_name="Tiene visibilidad?")
    ultimoticket= models.CharField(max_length=30, blank=False, null=False,verbose_name="Cuando es el ultimo ticket?")
    site=  models.BooleanField(default=False,help_text="Clikear si hay otro servicio en el sitio",verbose_name="Hay otro servicio en el mismo site?")
    bw= models.CharField(max_length=12, blank=True, null=True,verbose_name="Ancho de banda medio")
    picos=models.CharField(max_length=12, blank=True, null=True,verbose_name="Pico de ancho de banda")
    notes= models.TextField(blank=True, null=True,verbose_name="Comentarios")


    def __str__(self):
        return self.name
    
    