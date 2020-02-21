from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from adminka.model.room import Reservation


class ReservationsView(View):
    def get(self, request):
        rvs = Reservation.objects.all()
        return render(request, 'adminka/reservations/reservations.html', {'reservations': rvs})


class ReservationsCreateView(View):
    def get(self, request):
        return render(request, 'adminka/reservations/reservations_create.html')


class ReservationsUpdateView(View):
    def get(self, request):
        return render(request, 'adminka/reservations/reservations_update.html')


class ReservationsDeleteView(View):
    def get(self, request, id):
        r = Reservation.objects.get(id=id)
        r.delete()
        return HttpResponseRedirect(reverse('reservations'))
