from rest_framework import serializers
from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    host = serializers.ReadOnlyField(source='host.username')
    host_id = serializers.ReadOnlyField(source='host.id')

    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'description', 'price_per_night',
            'location', 'max_guests', 'bedrooms', 'bathrooms',
            'created_at', 'updated_at', 'host', 'host_id'
        ]
        read_only_fields = ['created_at', 'updated_at', 'host', 'host_id']
