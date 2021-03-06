# Generated by Django 2.2.7 on 2019-11-08 14:16

from django.db import migrations, models
import django.db.models.deletion

CURRENCIES = [
    {'code': 'CZK', 'name': 'Czech Republic Koruna'},
    {'code': 'EUR', 'name': 'Euro'},
    {'code': 'PLN', 'name': 'Polish Zloty'},
    {'code': 'USD', 'name': 'United States Dollar'}
]


def forwards(apps, schema_editor):
    # Creates all currencies
    # by the given task initially we need to have these 4 currencies
    Currency = apps.get_model("currencies", "Currency")
    for currency in CURRENCIES:
        Currency.objects.create(**currency)


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False, unique=True,
                                          verbose_name='Currency')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('rate', models.FloatField(verbose_name='Rate')),
                ('source_currency',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_currency',
                                   to='currencies.Currency', verbose_name='Source currency')),
                ('target_currency',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_currency',
                                   to='currencies.Currency', verbose_name='Target currency')),
            ],
            options={
                'verbose_name': 'Exchange Rate',
                'verbose_name_plural': 'Exchange Rates',
                'unique_together': {('source_currency', 'target_currency')},
            },
        ),
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]
