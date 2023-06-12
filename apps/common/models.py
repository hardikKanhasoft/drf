from django.db import models
from django.utils.translation import gettext_lazy as _

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(_("time of creation"), auto_now_add=True)
    updated = models.DateTimeField(_("time of updation"), auto_now=True)
    
    class Meta:
        abstract = True