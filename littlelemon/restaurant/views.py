from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class BookingViewSet(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]


class SingleBookingItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class MenuViewSet(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

