from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt

from adminka.model.car import Car, CarImage


class AdminCarsView(View):
    def get(self, request):
        if request.GET.get('q'):
            search_term = request.GET.get('q')
            if request.LANGUAGE_CODE == 'en':
                search_result = Car.objects.all().filter(title__title_en__icontains=search_term)
            else:
                search_result = Car.objects.all().filter(title__title_ru__icontains=search_term)

            return render(request, 'adminka/cars/cars.html', {'cars': search_result})

        cars = Car.objects.all()

        page = request.GET.get('page', 1)

        paginator = Paginator(cars, 15)
        try:
            cars = paginator.page(page)
        except PageNotAnInteger:
            cars = paginator.page(1)
        except EmptyPage:
            cars = paginator.page(paginator.num_pages)

        return render(request, 'adminka/cars/cars.html', {'cars': cars})


class CarsCreateView(View):
    def get(self, request):
        return render(request, 'adminka/cars/cars_create.html')

    def post(self, request):
        post = self.request.POST

        title_en = post.get('title_en')
        title_ar = post.get('title_ar')
        title_fa = post.get('title_fa')
        title_hi = post.get('title_hi')
        title_ru = post.get('title_ru')
        title_zh = post.get('title_zh')

        title = {
            'title_en': title_en,
            'title_ar': title_ar,
            'title_fa': title_fa,
            'title_hi': title_hi,
            'title_ru': title_ru,
            'title_zh': title_zh,
        }

        description_en = post.get('description_en')
        description_ar = post.get('description_ar')
        description_fa = post.get('description_fa')
        description_hi = post.get('description_hi')
        description_ru = post.get('description_ru')
        description_zh = post.get('description_zh')

        description = {
            'description_en': description_en,
            'description_ar': description_ar,
            'description_fa': description_fa,
            'description_hi': description_hi,
            'description_ru': description_ru,
            'description_zh': description_zh,
        }

        images = self.request.FILES.getlist('image')

        duration = post.get('duration')
        if not duration:
            duration = None

        price = post.get('price')
        if not price:
            price = None

        car = Car.objects.create(title=title, description=description, duration=duration, price=price)

        for i in images:
            CarImage.objects.create(image=i, car=car)

        return HttpResponseRedirect(reverse('adminka-cars'))


class CarsUpdateView(View):
    def get(self, request, id):
        car = Car.objects.get(id=id)
        c_images = CarImage.objects.filter(car=car)
        return render(request, 'adminka/cars/cars_update.html', {'car': car, 'c_images': c_images})

    def post(self, request, id):
        car = Car.objects.get(id=id)

        post = self.request.POST

        title_en = post.get('title_en')
        title_ar = post.get('title_ar')
        title_fa = post.get('title_fa')
        title_hi = post.get('title_hi')
        title_ru = post.get('title_ru')
        title_zh = post.get('title_zh')

        title = {
            'title_en': title_en,
            'title_ar': title_ar,
            'title_fa': title_fa,
            'title_hi': title_hi,
            'title_ru': title_ru,
            'title_zh': title_zh,
        }

        description_en = post.get('description_en')
        description_ar = post.get('description_ar')
        description_fa = post.get('description_fa')
        description_hi = post.get('description_hi')
        description_ru = post.get('description_ru')
        description_zh = post.get('description_zh')

        description = {
            'description_en': description_en,
            'description_ar': description_ar,
            'description_fa': description_fa,
            'description_hi': description_hi,
            'description_ru': description_ru,
            'description_zh': description_zh,
        }

        images = self.request.FILES.getlist('image')

        duration = post.get('duration')
        if not duration:
            duration = None

        price = post.get('price')
        if not price:
            price = None

        for i in images:
            obj, _ = CarImage.objects.get_or_create(image=i, car=car)

        car.title = title
        car.description = description
        car.duration = duration
        car.price = price
        car.save()

        return HttpResponseRedirect(reverse('adminka-cars'))


class CarsDeleteView(View):
    def get(self, request, id):
        car = Car.objects.get(id=id)
        car.delete()
        return HttpResponseRedirect(reverse('adminka-cars'))


@csrf_exempt
def car_image_delete(self):
    image = CarImage.objects.get(id=self.POST.get('key'))
    image.image.delete()
    image.delete()
    return HttpResponse('image deleted')
