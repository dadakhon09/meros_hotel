from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'main/index.html')

    # checkaviabilty():
    # roooms =Roon.objects.all()
    # for room in rooms:
    #     if now >= room.enddate:
    #         room.abialb=True

