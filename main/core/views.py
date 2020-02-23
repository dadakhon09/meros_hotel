from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from adminka.model import About, Room


class IndexView(View):
    def get(self, request):
        about = About.objects.get(id=1)
        room1 = Room.objects.filter(room_type=0).first()
        room2 = Room.objects.filter(room_type=1).first()
        room3 = Room.objects.filter(room_type=2).first()

        context = {
            'about': about,
            'room1': room1,
            'room2': room2,
            'room3': room3,
        }

        return render(request, 'main/index.html', context)
