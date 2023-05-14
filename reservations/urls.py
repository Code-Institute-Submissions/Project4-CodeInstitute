from django.urls import include, path

app_name = 'reservations'

urlpatterns = [
    path('reservations/', include('reservations.urls')),
]
