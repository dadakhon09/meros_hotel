from datetime import date

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from adminka.model.room import Reservation, Room


class ReservationsView(View):
    def get(self, request):
        if request.GET.get('q'):
            search_term = request.GET.get('q')
            if request.LANGUAGE_CODE == 'en':
                search_result = Reservation.objects.all().filter(room__title__title_en__icontains=search_term)
            else:
                search_result = Reservation.objects.all().filter(room__title__title_ru__icontains=search_term)

            return render(request, 'adminka/reservations/reservations.html', {'reservations': search_result})

        rvs = Reservation.objects.all()
        return render(request, 'adminka/reservations/reservations.html', {'reservations': rvs})


class ReservationsCreateView(View):
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, 'adminka/reservations/reservations_create.html', {'rooms': rooms})

    def post(self, request):
        room_id = self.request.POST.get('room')
        customer_name = self.request.POST.get('customer_name')
        customer_email = self.request.POST.get('customer_email')
        num_of_adults = self.request.POST.get('num_of_adults')
        num_of_children = self.request.POST.get('num_of_children')
        start_date = self.request.POST.get('start_date')
        end_date = self.request.POST.get('end_date')

        if not num_of_adults:
            num_of_adults = None

        if not num_of_children:
            num_of_children = None

        r = Reservation.objects.create(room_id=room_id, customer_name=customer_name, customer_email=customer_email,
                                       num_of_children=num_of_children, num_of_adults=num_of_adults,
                                       start_date=start_date, end_date=end_date)
        return HttpResponseRedirect(reverse('reservations'))


class ReservationsUpdateView(View):
    def get(self, request, id):
        r = Reservation.objects.get(id=id)
        rooms = Room.objects.exclude(id=r.room_id)
        return render(request, 'adminka/reservations/reservations_update.html', {'reservation': r, 'rooms': rooms})

    def post(self, request, id):
        res = Reservation.objects.get(id=id)
        room_id = self.request.POST.get('room')
        customer_name = self.request.POST.get('customer_name')
        customer_email = self.request.POST.get('customer_email')
        num_of_adults = self.request.POST.get('num_of_adults')
        num_of_children = self.request.POST.get('num_of_children')

        start_date = self.request.POST.get('start_date')
        start_date = start_date.split('/')
        start_date = date(year=int(start_date[2]), month=int(start_date[1]), day=int(start_date[0]))

        end_date = self.request.POST.get('end_date')
        print(end_date)
        end_date = end_date.split('/')
        end_date = date(year=int(end_date[2]), month=int(end_date[1]), day=int(end_date[0]))

        if not num_of_adults:
            num_of_adults = None

        if not num_of_children:
            num_of_children = None

        res.room_id = room_id
        res.customer_name = customer_name
        res.customer_email = customer_email
        res.num_of_adults = num_of_adults
        res.num_of_children = num_of_children
        res.start_date = start_date
        res.end_date = end_date
        res.save()

        return HttpResponseRedirect(reverse('reservations'))

class ReservationsDeleteView(View):
    def get(self, request, id):
        r = Reservation.objects.get(id=id)
        r.delete()
        return HttpResponseRedirect(reverse('reservations'))
