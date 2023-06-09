from django.db import models
from apps.common.constants import Role
# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=24)
    role = models.CharField(choices=Role.CHOICES)
    