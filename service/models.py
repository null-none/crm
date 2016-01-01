from __future__ import unicode_literals

from django.db import models

from common.models import *

class Service(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField(max_length=255)
    price = models.TextField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
