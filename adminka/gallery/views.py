from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from adminka.model import About, Gallery
from adminka.model.room import Room, RoomImage


class AdminGalleryView(LoginRequiredMixin, View):
    def get(self, request):
        gallery = Gallery.objects.all()

        context = {
            'gallery': gallery
        }

        return render(request, 'adminka/gallery/gallery.html', context)

    def post(self, request):

        images = self.request.FILES.getlist('image')

        for i in images:
            gi, _ = Gallery.objects.get_or_create(image=i)

        return HttpResponseRedirect(reverse('adminka-gallery'))


@csrf_exempt
def gallery_image_delete(self):
    image = Gallery.objects.get(id=self.POST.get('key'))
    image.image.delete()
    image.delete()
    return HttpResponse('image deleted')
