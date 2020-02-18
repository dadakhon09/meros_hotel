from datetime import datetime, date, timedelta

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from adminka.model.room import Room, RoomImage, Reservation


class RoomsView(View):
    def get(self, request):
        rooms = Room.objects.all()

        return render(request, 'main/accomodation.html', {'rooms': rooms})


class RoomView(View):
    def get(self, request, slug):
        room = Room.objects.get(slug=slug)
        r_images = RoomImage.objects.filter(room=room)
        return render(request, 'main/accomodation_view.html', {'room': room, 'r_images': r_images})


class AvailableRoomsView(View):
    def get(self, request, start_date, end_date):
        rooms = Room.objects.filter(availability=True)


class CheckAvailability(View):
    def post(self, request):
        start_date = self.request.POST.get('start_date')
        start_date = start_date.split('/')
        start_date = date(year=int(start_date[2]), month=int(start_date[1]), day=int(start_date[0]))
        end_date = self.request.POST.get('end_date')
        end_date = end_date.split('/')
        end_date = date(year=int(end_date[2]), month=int(end_date[1]), day=int(end_date[0]))
        num_of_adults = self.request.POST.get('num_of_adults')
        num_of_children = self.request.POST.get('num_of_children')

        rvs = Reservation.objects.select_related('room').exclude(
            start_date__lte=start_date
        ).exclude(start_date__gt=start_date, end_date__gte=end_date).exclude(start_date__gte=start_date,
                                                                             end_date__lte=end_date)

        # Q(start_date__lte=start_date) | Q(start_date__lt=end_date),
        # Q(end_date__lt=start_date) | Q(end_date__gte=end_date)
        print(rvs)

        return HttpResponse('asdasdsa')


class Book(View):
    def post(self, request):
        start_date = self.request.POST.get('start_date')
        # start_date = start_date.split('/')
        # start_date = date(year=int(start_date[2]), month=int(start_date[1]), day=int(start_date[0]))
        end_date = self.request.POST.get('end_date')
        # end_date = end_date.split('/')
        # end_date = date(year=int(end_date[2]), month=int(end_date[1]), day=int(end_date[0]))
        num_of_adults = self.request.POST.get('num_of_adults')
        num_of_children = self.request.POST.get('num_of_children')
        customer_name = self.request.POST.get('customer_name')
        customer_email = self.request.POST.get('customer_email')

        r = Reservation.objects.create(start_date=start_date, end_date=end_date, num_of_adults=num_of_adults,
                                       num_of_children=num_of_children, customer_email=customer_email,
                                       customer_name=customer_name)

        return redirect('')