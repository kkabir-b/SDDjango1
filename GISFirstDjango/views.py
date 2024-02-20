from django.shortcuts import render
from .models import Person

def splash(request):
    name = '2'
    people = Person.objects.all()
    debug_people = list(people)
    lst = ['a','b','c','d']
    return render(request, "splash.html", {'lst': lst,'name':name})