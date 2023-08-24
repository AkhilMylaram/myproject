from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Contacts(models.Model):
    name=models.CharField(max_length=40)
    phone_number=models.IntegerField()
    email_id=models.EmailField()
    address=models.TextField()

    def __str__(self):
        return f"Name : {self.name} PhNo: {self.phone_number}"

