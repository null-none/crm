from __future__ import unicode_literals

from django.db import models

from common.models import *

class Company(models.Model):
    name = models.CharField(max_length=255)
    country = models.ManyToManyField(Country)
    type = models.ManyToManyField(Type)
    description = models.TextField(max_length=255)
    info = models.TextField(max_length=255)
    feedback = models.TextField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
