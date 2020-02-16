from django.shortcuts import render
from django.views import View

from adminka.model.room import Room, RoomImage


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