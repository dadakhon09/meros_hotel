from django.shortcuts import render
from django.views import View

from adminka.model.sight import Sight


class SightsView(View):
    def get(self, request):
        sights = Sight.objects.all()
        return render(request, 'main/sights.html', {'sights': sights})


class SightView(View):
    def get(self, request, slug):
        sight = Sight.objects.get(slug=slug)

        return render(request, 'main/sight_view.html', {'slug': slug})
