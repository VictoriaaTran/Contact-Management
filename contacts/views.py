from django.shortcuts import render
from django.views.generic import ListView
from .models import Contact

#listing of all contacts
class ContactListView(ListView):
    model = Contact

