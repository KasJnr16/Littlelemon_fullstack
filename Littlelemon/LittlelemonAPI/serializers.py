from rest_framework import serializers
from .models import(
    MenuAPI,
    BookingAPI,
)

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuAPI
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingAPI
        fields = "__all__"