from django.db import models
from django.utils import timezone


class Employee(models.Model):
    name = models.CharField(max_length=150, blank=True)
    abbreviation = models.CharField(max_length=3, blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
