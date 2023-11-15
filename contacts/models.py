from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20, null=False, unique=True, error_messages={'unique':"Contact with this name already exists."})
    email = models.EmailField(null=False, unique=True, error_messages={
        'unique': "This email is already in use.",
        'required': "Email field cannot be empty.",
        'invalid': "Enter a valid email address."})
    notes = models.TextField(max_length = 200, default="", blank="True") #multiple lines of text
    created_time = models.DateTimeField(auto_now_add=True)
