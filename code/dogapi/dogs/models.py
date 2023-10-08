from django.db import models

# Create your models here.
class Dog(models.Model):
    first_name = models.CharField(max_length=30)
    breed = models.CharField(max_length=40)
    
    def __str__(self):
        return str(self.id)+ ":" + str(self.first_name)