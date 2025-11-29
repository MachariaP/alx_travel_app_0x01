from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    listing = ListingSerializer(read_only=True)
    listing_id = serializers.PrimaryKeyRelatedField(
        queryset=Listing.objects.all(), source='listing', write_only=True
    )
    guest = serializers.ReadOnlyField(source='guest.username')

    class Meta:
        model = Booking
        fields = [
            'id', 'listing', 'listing_id', 'guest',
            'check_in', 'check_out', 'total_price', 'created_at'
        ]
        read_only_fields = ['total_price', 'guest', 'created_at']
