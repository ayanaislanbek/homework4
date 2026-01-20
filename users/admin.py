from django.contrib import admin
from .models import DevUser, Location, HouseTour, TourRegistration

admin.site.register(DevUser)
admin.site.register(Location)
admin.site.register(HouseTour)
admin.site.register(TourRegistration)