from django.db import models
from django.core.exceptions import ValidationError
# from django.contrib.auth.models import User


class Users(models.Model):
    UserID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=255)
    UserType = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class Reservations(models.Model):
    ReservationID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(Users, on_delete=models.CASCADE)
    RestaurantID = models.ForeignKey('Restaurants', on_delete=models.CASCADE)
    TimeslotID = models.ForeignKey('Timeslots', on_delete=models.CASCADE)
    NumOfGuests = models.IntegerField()
    ReservationDate = models.DateField()

    def __str__(self):
        return f"Reservation ID: {self.ReservationID}"


class Restaurants(models.Model):
    RestaurantID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    PhoneNum = models.CharField(max_length=20)

    def __str__(self):
        return self.Name


class Timeslots(models.Model):
    TimeslotID = models.AutoField(primary_key=True)
    StartTime = models.TimeField()
    EndTime = models.TimeField()

    def __str__(self):
        return f"{self.StartTime} - {self.EndTime}"
