from django.contrib import admin
from .models import Users, Reservations, Restaurants, Timeslots


admin.site.register(Timeslots)


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('UserID', 'Name', 'Email', 'UserType')
    ordering = ('Name',)
    search_fields = ('Name', 'Email')


@admin.register(Reservations)
class ReservationsAdmin(admin.ModelAdmin):
    list_display = ('ReservationID', 'UserID', 'RestaurantID', 'TimeslotID',
                    'ReservationDate')
    ordering = ('ReservationID',)
    search_fields = ('ReservationID', 'RestaurantID__Name')
    list_filter = ('RestaurantID', 'TimeslotID', 'ReservationDate')


@admin.register(Restaurants)
class RestaurantsAdmin(admin.ModelAdmin):
    list_display = ('RestaurantID', 'Name', 'Address')
    ordering = ('Name',)
    list_filter = ('Name', 'Address')

