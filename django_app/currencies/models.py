from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import TimeStampedModel
from currencies.managers import CurrencyManager


class Currency(models.Model):
    code = models.CharField(_('Currency'), max_length=3, unique=True, primary_key=True)
    name = models.CharField(_('Name'), max_length=255)

    class Meta:
        verbose_name = _('Currency')
        verbose_name_plural = _('Currencies')

    objects = CurrencyManager()

    def __str__(self):
        return f'{self.code} - {self.name}'


class ExchangeRate(TimeStampedModel):
    source_currency = models.ForeignKey(Currency, verbose_name=_('Source currency'), related_name=_('source_currency'),
                                        on_delete=models.CASCADE)
    target_currency = models.ForeignKey(Currency, verbose_name=_('Target currency'), related_name=_('target_currency'),
                                        on_delete=models.CASCADE)
    rate = models.FloatField(_('Rate'))

    class Meta:
        verbose_name = _('Exchange Rate')
        verbose_name_plural = _('Exchange Rates')
        unique_together = ('source_currency', 'target_currency')

    def __str__(self):
        return f'1 {self.source_currency} = {self.rate} {self.target_currency}'
