from django.test import TestCase

# Create your tests here.
from models import user_database


user1 =user_database.objects.all

print(user1)