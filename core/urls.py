from django.contrib import admin
from django.urls import path, include

from booking.urls import urlpatterns as booking_urls
from graphql_pgd.urls import urlpatterns as garphql_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(booking_urls)),
    path('', include(garphql_urls)),
]
