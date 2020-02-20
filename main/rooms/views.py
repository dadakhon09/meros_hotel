from datetime import datetime, date, timedelta

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
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

        case_1 = Reservation.objects.filter(start_date__lte=start_date, end_date__gte=start_date).exists()

        case_2 = Reservation.objects.filter(start_date__lte=end_date, end_date__gte=end_date).exists()

        case_3 = Reservation.objects.filter(start_date__gte=start_date, end_date__lte=end_date).exists()

        print(case_1)
        print(case_2)
        print(case_3)

        case_1_q = Reservation.objects.filter(start_date__lte=start_date, end_date__gte=start_date)
        case_2_q = Reservation.objects.filter(start_date__lte=end_date, end_date__gte=end_date)
        case_3_q = Reservation.objects.filter(start_date__gte=start_date, end_date__lte=end_date)

        if case_1 is False and case_2 is False and case_3 is False:
            context = {
                'rvs': Reservation.objects.all()
            }
            return render(request, 'main/available_rooms.html', context)
        elif case_1 is False and case_2 is False:
            context = {
                'rvs': case_1_q.union(case_2_q)
            }
        elif case_1 is False and case_3 is False:
            context = {
                'rvs': case_1_q.union(case_3_q)
            }
        elif case_2 is False and case_3 is False:
            context = {
                'rvs': case_2_q.union(case_3_q)
            }
        elif not case_1:
            context = {
                'rvs': case_1_q.union(case_2_q)
            }
        elif not case_2:
            context = {
                'rvs': case_1_q.union(case_2_q)
            }
        elif not case_3:
            pass
        #
        # if case_1 or case_2 or case_3:
        #     # return render(request, "system/reserve.html",
        #     #               {"errors": "This room is not available on your selected dates"})
        #     return HttpResponse('error')
        return HttpResponse('asdasdsa')


class BookView(View):
    def post(self, request, room_id):
        room = Room.objects.get(id=room_id)

        start_date = self.request.POST.get('start_date')
        start_date = start_date.split('/')
        start_date = date(year=int(start_date[2]), month=int(start_date[1]), day=int(start_date[0]))
        end_date = self.request.POST.get('end_date')
        end_date = end_date.split('/')
        end_date = date(year=int(end_date[2]), month=int(end_date[1]), day=int(end_date[0]))
        num_of_adults = self.request.POST.get('num_of_adults')
        print(num_of_adults)
        num_of_children = self.request.POST.get('num_of_children')
        customer_name = self.request.POST.get('customer_name')
        customer_email = self.request.POST.get('customer_email')

        r = Reservation.objects.create(room=room, start_date=start_date, end_date=end_date,
                                       num_of_adults=int(num_of_adults),
                                       num_of_children=int(num_of_children), customer_email=customer_email,
                                       customer_name=customer_name)

        return HttpResponseRedirect(reverse('room-view', kwargs={'slug': room.slug}))
