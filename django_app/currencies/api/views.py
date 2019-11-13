from rest_framework.generics import ListAPIView

from rest_framework.permissions import IsAuthenticated

from currencies.api.serializers import CurrencySerializer, ExchangeRateSerializer
from currencies.models import Currency, ExchangeRate


class CurrencyListView(ListAPIView):
    queryset = Currency.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CurrencySerializer


class ExchangeRateListView(ListAPIView):
    queryset = ExchangeRate.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ExchangeRateSerializer
