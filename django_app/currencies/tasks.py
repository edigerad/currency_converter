from __future__ import absolute_import, unicode_literals

from config.celery import app
from currencies.models import ExchangeRate
from currencies.utils import generate_exchange_rates

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task(name='update_exchange_rates')
def update_exchange_rates():
    logger.info('Updating the exchange rates')
    for rate in generate_exchange_rates():
        exchange_rate, created = ExchangeRate.objects.get_or_create(source_currency=rate['source'],
                                                                    target_currency=rate['target'],
                                                                    rate=rate['rate'])
        if not created:
            exchange_rate.rate = rate['rate']
            exchange_rate.save(update_fields=['rate'])
    logger.info("Exchange rates are updated")
