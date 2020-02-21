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

    def post(self, request):
        room = self.request.POST.get('room')
        customer_name = self.request.POST.get('customer_name')
        customer_email = self.request.POST.get('customer_email')
        num_of_adults = self.request.POST.get('num_of_adults')
        num_of_children = self.request.POST.get('num_of_children')
        start_date = self.request.POST.get('start_date')
        end_date = self.request.POST.get('end_date')



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
