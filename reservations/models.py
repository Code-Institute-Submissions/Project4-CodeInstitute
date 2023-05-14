from django.db import models
from django.core.exceptions import ValidationError


class Users(models.Model):
    UserID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=255)
    UserType = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class ReservationsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class Reservations(models.Model):
    ReservationID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(Users, on_delete=models.CASCADE)
    RestaurantID = models.ForeignKey('Restaurants', on_delete=models.CASCADE)
    TableID = models.ForeignKey('Tables', on_delete=models.CASCADE)
    TimeslotID = models.ForeignKey('Timeslots', on_delete=models.CASCADE)
    NumOfGuests = models.IntegerField()
    ReservationDate = models.DateField()
    ReservationTime = models.TimeField()

    objects = ReservationsManager()

    def clean(self):
        # Check if there is an existing reservation for the selected table
        # and time slot
        existing_reservation = Reservations.objects.filter(
            TableID=self.TableID,
            TimeslotID=self.TimeslotID
        ).exists()

        if existing_reservation:
            raise ValidationError(
                "The table is already booked for this time slot.")

    def __str__(self):
        return f"Reservation ID: {self.ReservationID}"


class Restaurants(models.Model):
    RestaurantID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    PhoneNum = models.CharField(max_length=20)

    def __str__(self):
        return self.Name


class Tables(models.Model):
    TableID = models.AutoField(primary_key=True)
    RestaurantID = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    TableNum = models.IntegerField()
    MaxCapacity = models.IntegerField()

    def __str__(self):
        return f"Table ID: {self.TableID}"


class Timeslots(models.Model):
    TimeslotID = models.AutoField(primary_key=True)
    StartTime = models.TimeField()
    EndTime = models.TimeField()

    def __str__(self):
        return f"Timeslot ID: {self.TimeslotID}"
