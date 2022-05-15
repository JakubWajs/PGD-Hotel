from graphene_django import DjangoObjectType
from booking.models import HotelGuest, Room, Reservation, Payment


class HotelGuestType(DjangoObjectType):
    class Meta:
        model = HotelGuest
        fields = ('name', 'lastname', 'email', 'tel_number')


class RoomType(DjangoObjectType):
    class Meta:
        model = Room
        fields = ('room_number', 'min_vacancy', 'max_vacancy')


class ReservationType(DjangoObjectType):
    class Meta:
        model = Reservation
        fields = ('price',
                  'prepayment_price',
                  'number_of_guests',
                  'date_from',
                  'date_to',
                  'description',
                  'booking_status',
                  'hotel_guest',
                  'room',)


class PaymentType(DjangoObjectType):
    class Meta:
        model = Payment
        fields = ('payment_id',
                  'payment_method',
                  'issue_date',
                  'receipt_date',
                  'payment_status',
                  'prepayment',
                  'reservation',)




