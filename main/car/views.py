from django.shortcuts import render
from django.views import View

from adminka.model.car import Car

class CarsView(View):
    def get(self, request):
    	cars = Car.objects.all()
    	return render(request, 'main/cars.html', {'cars': cars})


class CarView(View):
	def get(self, request, slug):
		car = Car.objects.get(slug=slug)
		return render(request, 'main/car_view.html', {'car': car})