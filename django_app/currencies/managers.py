from django.db import models


class CurrencyQuerySet(models.QuerySet):
    def get_queryset(self):
        return self.get_queryset()


class CurrencyManager(models.Manager):
    def get_queryset(self):
        return CurrencyQuerySet(self.model, using=self._db)

    def get_currency_list(self):
        qs = self.values_list('code').all()
        return [i[0] for i in qs]
