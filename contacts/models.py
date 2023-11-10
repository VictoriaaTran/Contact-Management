from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20, null=False, unique=True, error_messages={'unique':"Name has already been taken"})
    email = models.EmailField(null=False, unique=True, error_messages={'unique':"Invalid email"})
    created_time = models.DateTimeField(auto_now_add=True)
