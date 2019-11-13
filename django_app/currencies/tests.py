from django.urls import reverse
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient

from django.conf.urls import include, url


class RecordTests(APITestCase, URLPatternsTestCase):
    fixtures = ['currencies.json', 'user.json', 'rates.json']
    urlpatterns = [
        url(r'^api/v0', include('rest_auth.urls')),
        url(r'^api/v0/currencies/', include('currencies.api.urls')),
    ]

    def test_currency_list(self):
        login_url = reverse('rest_login')
        login_data = {'username': 'admin', 'password': 'admin'}

        login_response = self.client.post(login_url, data=login_data, format='json')

        api_client = APIClient()
        api_client.credentials(HTTP_AUTHORIZATION='JWT ' + login_response.data.get('token'))

        url = reverse('currency_list')
        response = api_client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)

    def test_rates(self):
        login_url = reverse('rest_login')
        login_data = {'username': 'admin', 'password': 'admin'}

        login_response = self.client.post(login_url, data=login_data, format='json')

        api_client = APIClient()
        api_client.credentials(HTTP_AUTHORIZATION='JWT ' + login_response.data.get('token'))

        url = reverse('rates')
        response = api_client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 12)