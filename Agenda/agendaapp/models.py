from unittest.util import _MAX_LENGTH
from django.db import models

class Contacts(models.Model):
    name = models.CharField(max_length =30)
    phone_number = models.CharField(max_length=15)
    email= models.EmailField()

    def __str__(self) -> str:
        return self.email

#object relational mapping
#restful