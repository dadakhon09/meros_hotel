from django.contrib import admin

from adminka.model.room import Reservation
from adminka.models import About, Room, RoomImage, Gallery

admin.site.register(About)
admin.site.register(Room)
admin.site.register(RoomImage)
admin.site.register(Gallery)
admin.site.register(Reservation)
