from django.contrib import admin
from rental.models import Rental, Reservation

# Register your models here.
admin.site.register(Rental)
admin.site.register(Reservation)
