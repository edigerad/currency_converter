from django.urls import path

from currencies.api.views import CurrencyListView,ExchangeRateListView

urlpatterns = [
    path('list/', CurrencyListView.as_view(), name='currency_list'),
    path('rates/', ExchangeRateListView.as_view(), name='rates')
]
