from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils import timezone
from django.views import View

from adminka.model.room import Room, Reservation


class AdminIndexView(LoginRequiredMixin, View):
    def get(self, request):
        total_rooms = Room.objects.all().count()
        available_rooms = Room.objects.filter(reservation__isnull=True)
        reserved_rooms = Room.objects.filter(id=-1)

        for room in Room.objects.all():
            for res in Reservation.objects.select_related('room').filter(room=room):
                if res.start_date <= timezone.now().date() < res.end_date or res.start_date < timezone.now().date() <= res.end_date:
                    reserved_rooms = reserved_rooms.union(Room.objects.filter(id=res.room_id))
                else:
                    available_rooms = available_rooms.union(Room.objects.filter(id=res.room_id))

        available_rooms = available_rooms.difference(reserved_rooms)

        context = {
            'total_rooms': total_rooms,
            'available_rooms': available_rooms.count(),
            'reserved_rooms': reserved_rooms.count(),
        }

        return render(request, 'adminka/index.html', context)
