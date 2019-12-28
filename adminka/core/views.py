from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from adminka.model.room import Villa
from adminka.model.tour import Tour
from adminka.model.sight import Sight
from adminka.model.news import News
from adminka.model.car import Car


class AdminIndexView(LoginRequiredMixin, View):
    def get(self, request):
        villas = Villa.objects.all().count()
        tours = Tour.objects.all().count()
        sights = Sight.objects.all().count()
        news = News.objects.all().count()
        cars = Car.objects.all().count()

        context = {
            'villas': villas,
            'tours': tours,
            'sights': sights,
            'news': news,
            'cars': cars
        }
        return render(request, 'adminka/index.html', context)
