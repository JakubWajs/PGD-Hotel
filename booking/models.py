from django.db import models
from django.utils.timezone import now
import uuid


class HotelGuest(models.Model):
    name = models.CharField(max_length=46, default='noname')
    lastname = models.CharField(max_length=46, default='noname')
    email = models.EmailField(max_length=254)
    tel_number = models.CharField(max_length=12, blank=True, null=True)


class Room(models.Model):
    room_number = models.PositiveSmallIntegerField()
    min_vacancy = models.PositiveSmallIntegerField(default=1)
    max_vacancy = models.PositiveSmallIntegerField(default=7)


class Reservation(models.Model):
    BOOKING_STATUS = {
        (0, 'Do zatwierdzenia'),
        (1, 'Zatwierdzona'),
        (2, 'Zrealizowana'),
        (3, 'Anulowana'),
    }

    price = models.FloatField(default=0)
    prepayment_price = models.FloatField(default=0, blank=True, null=True)
    number_of_guests = models.PositiveSmallIntegerField()
    date_from = models.DateField(default=now)
    date_to = models.DateField(default=now)
    description = models.TextField(blank=True, null=True)
    booking_status = models.PositiveSmallIntegerField(default=0, choices=BOOKING_STATUS)

    hotel_guest = models.ForeignKey(HotelGuest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


class Payment(models.Model):
    PAYMENT_METHOD = {
        (0, 'Przelew'),
        (1, 'Gotówka'),
        (2, 'Airbnb'),
        (3, 'Aplikacja'),
    }

    payment_id = models.UUIDField(primary_key=True,
                                  default=uuid.uuid4,
                                  editable=False)

    payment_method = models.PositiveSmallIntegerField(choices=PAYMENT_METHOD)
    issue_date = models.DateField(auto_now=True)
    receipt_date = models.DateField()
    payment_status = models.BooleanField(default=False)
    prepayment = models.BooleanField(default=False)

    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
