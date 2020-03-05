from django.shortcuts import render
from django.views import View

from adminka.model import About


class AboutView(View):
    def get(self, request):
        about = About.objects.get(id=1)
        return render(request, 'main/about.html', {'about': about})
