from django.db import models

# Create your models here.

class Users(models.Model):
    email = models.CharField(max_length = 200)
    user_name = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    fname = models.CharField(max_length = 200)
    lname = models.CharField(max_length = 200)
