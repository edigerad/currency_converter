from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimeStampedModel(models.Model):
    created_date = models.DateTimeField(_('Created date'), auto_now_add=True)
    updated_date = models.DateTimeField(_('Updated date'), auto_now=True)

    class Meta:
        abstract = True
