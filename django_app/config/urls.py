from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v0/', include('rest_auth.urls')),
    path('api/v0/currencies/', include('currencies.api.urls')),
]
