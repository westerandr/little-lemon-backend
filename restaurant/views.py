from django.shortcuts import render
from rest_framework import generics
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User

# Create your views here.
def index(request):
  return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
  serializer_class = MenuSerializer
  queryset = Menu.objects.all()
  permission_classes = [permissions.IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
  serializer_class = MenuSerializer
  queryset = Menu.objects.all()

class BookingViewSet(viewsets.ModelViewSet):
  serializer_class = BookingSerializer
  queryset = Booking.objects.all()
  permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
  serializer_class = UserSerializer
  queryset = User.objects.all()
  permission_classes = [permissions.IsAuthenticated]