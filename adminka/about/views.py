from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from adminka.model.about import About


class AdminAboutView(LoginRequiredMixin, View):
    def get(self, request):
        about = About.objects.get(id=1)
        return render(request, 'adminka/about/about.html', {'about': about})

    def post(self, request):
        about = About.objects.get(id=1)

        post = self.request.POST

        text_en = post.get('text_en')
        text_ru = post.get('text_ru')

        text = {
            'text_en': text_en,
            'text_ru': text_ru
        }

        image = self.request.FILES.get('image')

        about.text = text

        if about.image and about.image != image:
            about.save()
        else:
            about.image = image
        about.save()

        # for i in images:
        #     ai, _ = AboutImage.objects.get_or_create(image=i, about=about)

        return HttpResponseRedirect(reverse('adminka-index'))


@csrf_exempt
def about_image_delete(self):
    about = About.objects.get(id=1)
    about.image.delete()
    return HttpResponse('image deleted')
