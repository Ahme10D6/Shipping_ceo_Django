from django.shortcuts import render
from .models import Shipping ,Tracking

# Create your views here.
def ship(request):
    return render(request,'services/ship.html')
def ships(request):
    return render(request,'services/ships.html',{'ships':Shipping.objects.all()})
