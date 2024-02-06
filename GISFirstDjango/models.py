from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    luck = models.IntegerField()
    age = models.IntegerField(blank=False, null=True)
    would_you_win = models.BooleanField()

class TeachingGroup(models.Model):
    name = models.CharField(max_length=30, null=True)
    students = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)
    year_group = models.IntegerField(blank=False, null=True)

