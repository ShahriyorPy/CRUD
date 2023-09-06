from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50,verbose_name="ism")
    phone = models.CharField(max_length=17,verbose_name="telefon")

    def __str__(self):
        return self.name

