from django.shortcuts import render
from .models import Reservations
from .forms import UsersForm


def index(request):
    return render(request, 'index.html')


def reservations(request):
    reservations_list = Reservations.objects.all()
    return render(request, 'reservations.html',
                  {'reservations_list': reservations_list})


def signup(request):
    return render(request, 'signup.html', {})
