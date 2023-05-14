from django.shortcuts import render
from .models import Reservations


def index(request):
    return render(request, 'index.html')


def reservations(request):
    reservations_list = Reservations.objects.all()
    return render(request, 'reservations.html',
                  {'reservations_list': reservations_list})