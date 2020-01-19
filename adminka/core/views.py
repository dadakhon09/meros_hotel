from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from adminka.model.room import Room


class AdminIndexView(LoginRequiredMixin, View):
    def get(self, request):
        rooms = Room.objects.all().count()

        context = {
            'rooms': rooms
        }
        return render(request, 'adminka/index.html', context)
