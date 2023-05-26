from django.shortcuts import render, redirect
from .models import Reservations
from .forms import UsersForm, UpdateForm, CreateReservation
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'index.html')


def reservations(request):
    reservations_list = Reservations.objects.all()
    return render(request, 
                  'reservations.html',
                  {'reservations_list': reservations_list})


def signup(request):
    submitted = False
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('./?submitted=True')
    else:
        form = UsersForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'signup.html', {'form': form,
                                           'submitted': submitted})


def update_reservation(request, reservation_id):
    reservation = Reservations.objects.get(pk=reservation_id)
    form = UpdateForm(request.POST or None, instance=reservation)
    if form.is_valid():
        form.save()
        return redirect('reservations')
    return render(request,
                  'update_reservation.html',
                  {'reservation': reservation, 'form': form})

def create_reservation(request):
    submitted = False
    if request.method == "POST":
        form = CreateReservation(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('./?submitted=True')
    else:
        form = CreateReservation
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'create_reservation.html', {'form': form,
                                           'submitted': submitted})
