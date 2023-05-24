from django.shortcuts import render
from .models import Reservations
from .forms import UsersForm
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'index.html')


def reservations(request):
    reservations_list = Reservations.objects.all()
    return render(request, 'reservations.html',
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
