from django.shortcuts import render
from django.views import View

from adminka.model.tour import Tour


class ToursView(View):
    def get(self, request):
        tours = Tour.objects.all()

        return render(request, 'main/tours.html', {'tours': tours})


class TourView(View):
    def get(self, request, slug):
        tour = Tour.objects.get(slug=slug)
        return render(request, 'main/tour_view.html', {'tour': tour})
