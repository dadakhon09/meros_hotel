from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt

from adminka.model.sight import Sight, SightCategory, SightImage


class AdminSightsView(View):
    def get(self, request):
        if request.GET.get('q'):
            search_term = request.GET.get('q')
            if request.LANGUAGE_CODE == 'en':
                search_result = Sight.objects.all().filter(title__title_en__icontains=search_term)
            else:
                search_result = Sight.objects.all().filter(title__title_ru__icontains=search_term)

            return render(request, 'adminka/sights/sights.html', {'sights': search_result})

        sights = Sight.objects.all()

        page = request.GET.get('page', 1)

        paginator = Paginator(sights, 15)
        try:
            sights = paginator.page(page)
        except PageNotAnInteger:
            sights = paginator.page(1)
        except EmptyPage:
            sights = paginator.page(paginator.num_pages)

        return render(request, 'adminka/sights/sights.html', {'sights': sights})


class SightsCreateView(View):
    def get(self, request):
        s_categories = SightCategory.objects.all()
        return render(request, 'adminka/sights/sights_create.html', {'s_categories': s_categories})

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

        c = post.get('category')
        if c:
            category = SightCategory.objects.get(id=c)
        else:
            category = None

        images = self.request.FILES.getlist('image')

        sight = Sight.objects.create(title=title, description=description, category=category)

        for i in images:
            si = SightImage.objects.create(image=i, sight=sight)
            sight.s_images.add(si)
            sight.save()

        return HttpResponseRedirect(reverse('adminka-sights'))


class SightsUpdateView(View):
    def get(self, request, id):
        sight = Sight.objects.get(id=id)
        if sight.category:
            s_categories = SightCategory.objects.exclude(id=sight.category.id)
        else:
            s_categories = SightCategory.objects.all()

        s_images = SightImage.objects.filter(sight=sight)
        return render(request, 'adminka/sights/sights_update.html',
                      {'sight': sight, 's_categories': s_categories, 's_images': s_images})

    def post(self, request, id):
        sight = Sight.objects.get(id=id)
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

        c = post.get('category')
        if c:
            category = SightCategory.objects.get(id=c)
        else:
            category = None

        images = self.request.FILES.getlist('images')

        sight.title = title
        sight.description = description
        sight.category = category
        sight.save()

        for i in images:
            si = SightImage.objects.create(image=i, sight=sight)
            sight.images.add(si)
            sight.save()

        return HttpResponseRedirect(reverse('adminka-sights'))


class SightsDeleteView(View):
    def get(self, request, id):
        c = SightCategory.objects.get(id=id)
        c.delete()
        return HttpResponseRedirect(reverse('adminka-sights'))


class SightsCategoriesView(View):
    def get(self, request):
        if request.GET.get('q'):
            search_term = request.GET.get('q')
            if request.LANGUAGE_CODE == 'en':
                search_result = SightCategory.objects.all().filter(title__title_en__icontains=search_term)
            else:
                search_result = SightCategory.objects.all().filter(title__title_ru__icontains=search_term)

            return render(request, 'adminka/sights/sight_categories.html', {'s_categories': search_result})

        s_categories = SightCategory.objects.all()

        page = request.GET.get('page', 1)

        paginator = Paginator(s_categories, 15)
        try:
            s_categories = paginator.page(page)
        except PageNotAnInteger:
            s_categories = paginator.page(1)
        except EmptyPage:
            s_categories = paginator.page(paginator.num_pages)

        return render(request, 'adminka/sights/sight_categories.html', {'s_categories': s_categories})


class SightsCategoriesCreateView(View):
    def get(self, request):
        return render(request, 'adminka/sights/sight_categories_create.html')

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

        SightCategory.objects.create(title=title)

        return HttpResponseRedirect(reverse('sight-categories'))


class SightsCategoriesUpdateView(View):
    def get(self, request, id):
        s_category = SightCategory.objects.get(id=id)
        return render(request, 'adminka/sights/sight_categories_update.html', {'s_category': s_category})

    def post(self, request, id):
        s_category = SightCategory.objects.get(id=id)

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

        s_category.title = title
        s_category.save()

        return HttpResponseRedirect(reverse('sight-categories'))


class SightsCategoriesDeleteView(View):
    def get(self, request, id):
        c = SightCategory.objects.get(id=id)

        c.delete()
        return HttpResponseRedirect(reverse('sight-categories'))


@csrf_exempt
def sight_image_delete(self):
    image = SightImage.objects.get(id=self.POST.get('key'))
    image.image.delete()
    image.delete()
    return HttpResponse('image deleted')
