from django.urls import path

from booking.views import testview


urlpatterns = [
    path("booking/", testview),
]
