from django.shortcuts import render
from django.views import View

from adminka.model.room import Room


class RoomsView(View):
    def get(self, request):
        rooms = Room.objects.all()

        return render(request, 'main/accomodation.html', {'rooms': rooms})


class RoomView(View):
    def get(self, request, slug):
        room = Room.objects.get(slug=slug)

        return render(request, 'main/accomodation.html', {'room': room})
