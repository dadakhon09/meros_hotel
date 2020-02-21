from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from adminka.model.room import Reservation, Room


class ReservationsView(View):
    def get(self, request):
        rvs = Reservation.objects.all()
        return render(request, 'adminka/reservations/reservations.html', {'reservations': rvs})


class ReservationsCreateView(View):
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, 'adminka/reservations/reservations_create.html', {'rooms': rooms})


class ReservationsUpdateView(View):
    def get(self, request, id):
        r = Reservation.objects.get(id=id)
        rooms = Room.objects.exclude(id=r.room_id)
        return render(request, 'adminka/reservations/reservations_update.html', {'reservation': r, 'rooms': rooms})


class ReservationsDeleteView(View):
    def get(self, request, id):
        r = Reservation.objects.get(id=id)
        r.delete()
        return HttpResponseRedirect(reverse('reservations'))
