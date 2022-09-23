from django.db import models

# Create your models here.

class user_database(models.Model):
    
    name = models.CharField(max_length=60)
    last_name=models.CharField(max_length=60)
    email = models.EmailField()
    password= models.CharField(max_length=250)

    def __str__(self)-> str:
        return self.name 


