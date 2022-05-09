from django.contrib import admin
from .models import HotelGuest, Room, Reservation, Payment


@admin.register(HotelGuest)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'lastname',
                    'email',
                    'tel_number')

    search_fields = ('lastname',
                     'email',
                     'tel_number')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number',
                    'min_vacancy',
                    'max_vacancy')

    list_filter = ('room_number',)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('booking_status',
                    'price',
                    'number_of_guests',
                    'date_from',
                    'date_to')

    list_filter = ('booking_status',
                   'number_of_guests')

    search_fields = ('hotel_guest',)

    ordering = ('price',
                'date_from',
                'date_to')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id',
                    'payment_status',
                    'prepayment',
                    'payment_method',
                    'issue_date',
                    'receipt_date')

    list_filter = ('payment_status',
                   'prepayment',
                   'payment_method')

    search_fields = ('payment_id',)

    ordering = ('issue_date',
                'receipt_date')
