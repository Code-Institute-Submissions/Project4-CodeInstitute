from django.contrib import admin
from .models import Users, Reservations, Restaurants, Tables, Timeslots

admin.site.register(Users)
admin.site.register(Reservations)
admin.site.register(Restaurants)
admin.site.register(Tables)
admin.site.register(Timeslots)
