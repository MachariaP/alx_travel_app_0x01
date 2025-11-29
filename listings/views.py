from rest_framework import viewsets
from .models import Listing
from .serializers import ListingSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ListingViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations for Listings.
    """
    queryset = Listing.objects.all().order_by('-created_at')
    serializer_class = ListingSerializer

    # Optional: Add custom swagger tags
    @swagger_auto_schema(tags=['Listings'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Listings'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Listings'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Listings'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Listings'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Listings'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
