from django.shortcuts import render
from django.views import View

from adminka.model.room import RoomImage


class GalleryView(View):
    def get(self, request):
        r_images = RoomImage.objects.all()

        return render(request, 'main/gallery.html', {'r_images': r_images})
