from django.shortcuts import render
from django.views import View

from adminka.model.villa import Villa


class VillasView(View):
    def get(self, request):
        villas = Villa.objects.all()

        return render(request, 'main/villas.html', {'villas': villas})


class VillaView(View):
    def get(self, request, slug):
        villa = Villa.objects.get(slug=slug)

        return render(request, 'main/villa_view.html', {'villa': villa})
