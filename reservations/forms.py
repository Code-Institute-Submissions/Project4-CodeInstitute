from django import forms
from django.forms import ModelForm
from .models import Users, Reservations, Timeslots, Restaurants


# Create a new user
class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ('Name', 'Email', 'Password')

        widgets = {
            'Name':
            forms.TextInput(attrs={'class': 'form-control',
                                   'placeholder': 'Enter your name'}),
            'Email':
            forms.EmailInput(attrs={'class': 'form-control',
                                    'placeholder': 'Enter your email'}),
            'Password':
            forms.PasswordInput(attrs={'class': 'form-control',
                                       'placeholder': 'Enter your password'}),
            }


# Update Reservation form
class UpdateForm(ModelForm):
    TimeslotID = forms.ModelChoiceField(
        queryset=Timeslots.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Reservation Time',
        to_field_name='StartTime',
    )

    class Meta:
        model = Reservations
        fields = ('ReservationDate', 'TimeslotID', 'NumOfGuests')
        labels = {
            'ReservationDate': 'Reservation Date',
            'NumOfGuests': '# of Guest',
        }

        widgets = {
            'ReservationDate':
            forms.DateInput(attrs={'class': 'form-control',
                                   'placeholder': 'Reservation Date'}),
            'TimeslotID':
            forms.TimeInput(attrs={'class': 'form-control',
                                   'placeholder': 'Reservation Time'}),
            'NumOfGuests':
            forms.NumberInput(attrs={'min': '1', 'max': '4',
                                     'class': 'form-control',
                                     'placeholder': '# of Guests'}),
        }

# Create a new reservation
class CreateReservation(ModelForm):
    RestaurantID = forms.ModelChoiceField(
        queryset=Restaurants.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Restaurant',
        to_field_name='Name'
    )

    TimeslotID = forms.ModelChoiceField(
        queryset=Timeslots.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Reservation Time',
        to_field_name='StartTime',
    )

    UserID = forms.ModelChoiceField(
        queryset=Users.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Name',
        to_field_name='Name'
    )

    class Meta:
        model = Reservations
        fields = ('UserID', 'RestaurantID', 
                  'ReservationDate', 'TimeslotID',
                  'NumOfGuests')
        labels = {
            'ReservationDate': 'Date',
            'NumOfGuests': '# of Guest',
        }

        widgets = {
            'RestaurantId':
            forms.Select(attrs={'class': 'form-control'}),
            'ReservationDate':
            forms.DateInput(attrs={'class': 'form-control',
                                   'placeholder': 'YYYY-MM-DD'}),
            'TimeslotID':
            forms.TimeInput(attrs={'class': 'form-control',
                                    'placeholder': 'Time'}),
            'NumOfGuests':
            forms.NumberInput(attrs={'min': '1', 'max': '10',
                                     'class': 'form-control'}),
        }
