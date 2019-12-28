from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt

from adminka.model.room import Villa, VillaService, VillaServiceCategory, VillaImage


class AdminVillasView(View):
    def get(self, request):
        if request.GET.get('q'):
            search_term = request.GET.get('q')
            if request.LANGUAGE_CODE == 'en':
                search_result = Villa.objects.all().filter(title__title_en__icontains=search_term)
            else:
                search_result = Villa.objects.all().filter(title__title_ru__icontains=search_term)

            return render(request, 'adminka/villas/villas.html', {'villas': search_result})

        villas = Villa.objects.all()

        page = request.GET.get('page', 1)

        paginator = Paginator(villas, 15)
        try:
            villas = paginator.page(page)
        except PageNotAnInteger:
            villas = paginator.page(1)
        except EmptyPage:
            villas = paginator.page(paginator.num_pages)

        return render(request, 'adminka/villas/villas.html', {'villas': villas})


class VillasCreateView(View):
    def get(self, request):
        v_services = VillaService.objects.all()
        v_service_categories = VillaServiceCategory.objects.all()
        return render(request, 'adminka/villas/villas_create.html',
                      {'v_service_categories': v_service_categories, 'v_services': v_services})

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

        address_en = post.get('address_en')
        address_ar = post.get('address_ar')
        address_fa = post.get('address_fa')
        address_hi = post.get('address_hi')
        address_ru = post.get('address_ru')
        address_zh = post.get('address_zh')

        address = {
            'address_en': address_en,
            'address_ar': address_ar,
            'address_fa': address_fa,
            'address_hi': address_hi,
            'address_ru': address_ru,
            'address_zh': address_zh,
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

        phone = post.get('phone')

        status = post.get('status')

        v_services = post.getlist('v_services')

        bedroom = post.get('bedroom')
        if not bedroom:
            bedroom = None

        square_meter = post.get('square_meter')
        if not square_meter:
            square_meter = None

        d_center = post.get('d_center')
        if not d_center:
            d_center = None

        d_railways = post.get('d_railways')
        if not d_railways:
            d_railways = None

        d_airways = post.get('d_airways')
        if not d_airways:
            d_airways = None

        images = self.request.FILES.getlist('image')

        villa = Villa.objects.create(title=title, address=address, description=description, phone=phone, status=status,
                                     bedroom=bedroom, square_meter=square_meter, d_airways=d_airways,
                                     d_railways=d_railways, d_center=d_center)

        for s in v_services:
            obj = VillaService.objects.get(id=s)
            obj.villas.add(villa)
            obj.save()

        villa.save()

        for i in images:
            VillaImage.objects.create(image=i, villa=villa)

        return HttpResponseRedirect(reverse('adminka-villas'))


class VillasUpdateView(View):
    def get(self, request, id):
        villa = Villa.objects.get(id=id)
        v_services = VillaService.objects.all()
        v_service_categories = VillaServiceCategory.objects.all()
        v_images = VillaImage.objects.filter(villa=villa)
        return render(request, 'adminka/villas/villas_update.html',
                      {'villa': villa, 'v_images': v_images, 'v_services': v_services,
                       'v_service_categories': v_service_categories})

    def post(self, request, id):
        villa = Villa.objects.get(id=id)

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

        address_en = post.get('address_en')
        address_ar = post.get('address_ar')
        address_fa = post.get('address_fa')
        address_hi = post.get('address_hi')
        address_ru = post.get('address_ru')
        address_zh = post.get('address_zh')

        address = {
            'address_en': address_en,
            'address_ar': address_ar,
            'address_fa': address_fa,
            'address_hi': address_hi,
            'address_ru': address_ru,
            'address_zh': address_zh,
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

        phone = post.get('phone')

        status = post.get('status')

        v_services = post.getlist('v_services')

        images = self.request.FILES.getlist('image')

        bedroom = post.get('bedroom')
        if not bedroom:
            bedroom = None

        square_meter = post.get('square_meter')
        if not square_meter:
            square_meter = None

        d_center = post.get('d_center')
        if not d_center:
            d_center = None

        d_railways = post.get('d_railways')
        if not d_railways:
            d_railways = None

        d_airways = post.get('d_airways')
        if not d_airways:
            d_airways = None

        villa.title = title
        villa.address = address
        villa.description = description
        villa.phone = phone
        villa.status = status
        villa.bedroom = bedroom
        villa.square_meter = square_meter
        villa.d_center = d_center
        villa.d_railways = d_railways
        villa.d_airways = d_airways

        villa.v_services.clear()
        for s in v_services:
            obj = VillaService.objects.get(id=s)
            obj.villas.add(villa)
            obj.save()

        villa.save()

        for i in images:
            vi, _ = VillaImage.objects.get_or_create(image=i, villa=villa)

        return HttpResponseRedirect(reverse('adminka-villas'))


class VillasDeleteView(View):
    def get(self, request, id):
        v = Villa.objects.get(id=id)
        v.delete()
        return HttpResponseRedirect(reverse('adminka-villas'))


class VillaServicesView(View):
    def get(self, request):
        if request.GET.get('q'):
            search_term = request.GET.get('q')
            if request.LANGUAGE_CODE == 'en':
                search_result = VillaService.objects.all().filter(title__title_en__icontains=search_term)
            else:
                search_result = VillaService.objects.all().filter(title__title_ru__icontains=search_term)

            return render(request, 'adminka/villas/villa_services.html', {'v_services': search_result})

        v_services = VillaService.objects.all()

        page = request.GET.get('page', 1)

        paginator = Paginator(v_services, 15)
        try:
            v_services = paginator.page(page)
        except PageNotAnInteger:
            v_services = paginator.page(1)
        except EmptyPage:
            v_services = paginator.page(paginator.num_pages)

        return render(request, 'adminka/villas/villa_services.html', {'v_services': v_services})


class VillaServicesCreateView(View):
    def get(self, request):
        v_service_categories = VillaServiceCategory.objects.all()
        return render(request, 'adminka/villas/villa_services_create.html',
                      {'v_service_categories': v_service_categories})

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

        c = post.get('category')
        if c:
            category = VillaServiceCategory(id=c)
        else:
            category = None

        VillaService.objects.create(title=title, category=category)

        return HttpResponseRedirect(reverse('villa-services'))


class VillaServicesUpdateView(View):
    def get(self, request, id):
        v_service = VillaService.objects.get(id=id)

        if v_service.category:
            v_service_categories = VillaServiceCategory.objects.exclude(id=v_service.category.id)
        else:
            v_service_categories = VillaServiceCategory.objects.all()
        return render(request, 'adminka/villas/villa_services_update.html',
                      {'v_service': v_service, 'v_service_categories': v_service_categories})

    def post(self, request, id):
        v_service = VillaService.objects.get(id=id)

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

        c = post.get('category')
        if c:
            category = VillaServiceCategory(id=c)
        else:
            category = None

        v_service.title = title
        v_service.category = category
        v_service.save()
        return HttpResponseRedirect(reverse('villa-services'))


class VillaServicesDeleteView(View):
    def get(self, request, id):
        v = VillaService.objects.get(id=id)
        v.delete()
        return HttpResponseRedirect(reverse('villa-services'))


class VillaServiceCategoriesView(View):
    def get(self, request):
        if request.GET.get('q'):
            search_term = request.GET.get('q')
            if request.LANGUAGE_CODE == 'en':
                search_result = VillaServiceCategory.objects.all().filter(title__title_en__icontains=search_term)
            else:
                search_result = VillaServiceCategory.objects.all().filter(title__title_ru__icontains=search_term)
            return render(request, 'adminka/villas/villa_service_categories.html',
                          {'v_service_categories': search_result})

        v_service_categories = VillaServiceCategory.objects.all()

        page = request.GET.get('page', 1)

        paginator = Paginator(v_service_categories, 15)
        try:
            v_service_categories = paginator.page(page)
        except PageNotAnInteger:
            v_service_categories = paginator.page(1)
        except EmptyPage:
            v_service_categories = paginator.page(paginator.num_pages)

        return render(request, 'adminka/villas/villa_service_categories.html',
                      {'v_service_categories': v_service_categories})


class VillaServiceCategoriesCreateView(View):
    def get(self, request):
        return render(request, 'adminka/villas/villa_service_categories_create.html')

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

        VillaServiceCategory.objects.create(title=title)

        return HttpResponseRedirect(reverse('villa-service-categories'))


class VillaServiceCategoriesUpdateView(View):
    def get(self, request, id):
        v_service_category = VillaServiceCategory.objects.get(id=id)
        return render(request, 'adminka/villas/villa_service_categories_update.html',
                      {'v_service_category': v_service_category})

    def post(self, request, id):
        v_service_category = VillaServiceCategory.objects.get(id=id)

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

        v_service_category.title = title
        v_service_category.save()

        return HttpResponseRedirect(reverse('villa-service-categories'))


class VillaServiceCategoriesDeleteView(View):
    def get(self, request, id):
        v = VillaServiceCategory.objects.get(id=id)
        v.delete()
        return HttpResponseRedirect(reverse('villa-service-categories'))


@csrf_exempt
def villa_image_delete(self):
    image = VillaImage.objects.get(id=self.POST.get('key'))
    image.image.delete()
    image.delete()
    return HttpResponse('image deleted')
