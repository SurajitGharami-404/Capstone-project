from rest_framework import generics, viewsets, permissions
from .serializers import MenuSerializers, BookingSerializers
from .models import Menu, Booking

# Create your views here.

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
    permission_classes = [permissions.IsAuthenticated]