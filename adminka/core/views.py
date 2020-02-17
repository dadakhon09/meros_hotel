from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from adminka.model.room import Room


class AdminIndexView(LoginRequiredMixin, View):
    def get(self, request):
        total_rooms = Room.objects.all().count()
        available_rooms = Room.objects.filter(availability=True).count()
        reserved_rooms = Room.objects.filter(availability=False).count()

        context = {
            'total_rooms': total_rooms,
            'available_rooms': available_rooms,
            'reserved_rooms': reserved_rooms,
        }

        return render(request, 'adminka/index.html', context)
