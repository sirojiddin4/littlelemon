from rest_framework import serializers
from .models import Booking, Menu

class Bookingserializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['first_name', 'reservations_date', 'reservations_slot']

class MenuBookingserializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['name', 'price', 'menu_item_description']