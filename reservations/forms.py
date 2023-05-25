from django import forms
from django.forms import ModelForm
from .models import Users, Reservations, Timeslots


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
