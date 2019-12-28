from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt

from adminka.model.tour import Tour, TourExpense, TourFacility, TourImage
from adminka.tours.get_icons import Icons

obj = Icons()
my_tuple = obj.get_icons()


class AdminToursView(View):
    def get(self, request):
        if request.GET.get('q'):
            search_term = request.GET.get('q')
            if request.LANGUAGE_CODE == 'en':
                search_result = Tour.objects.all().filter(title__title_en__icontains=search_term)
            else:
                search_result = Tour.objects.all().filter(title__title_ru__icontains=search_term)

            return render(request, 'adminka/tours/tours.html', {'tours': search_result})

        tours = Tour.objects.all()
        
        page = request.GET.get('page', 1)

        paginator = Paginator(tours, 15)
        try:
            tours = paginator.page(page)
        except PageNotAnInteger:
            tours = paginator.page(1)
        except EmptyPage:
            tours = paginator.page(paginator.num_pages)

        return render(request, 'adminka/tours/tours.html', {'tours': tours})


class ToursCreateView(View):
    def get(self, request):
        t_expenses = TourExpense.objects.all()
        t_facilities = TourFacility.objects.all()

        return render(request, 'adminka/tours/tours_create.html',
                      {'t_expenses': t_expenses, 't_facilities': t_facilities})

    def post(self, request):

        post = self.request.POST

        title_en = post.get('title_en')
        title_ar = post.get('title_ar')
        title_fa = post.get('title_fa')
        title_hi = post.get('title_hi')
        title_ru = post.get('title_ru')
        title_zh = post.get('title_zh')

        plan_en = post.get('plan_en')
        plan_ar = post.get('plan_ar')
        plan_fa = post.get('plan_fa')
        plan_hi = post.get('plan_hi')
        plan_ru = post.get('plan_ru')
        plan_zh = post.get('plan_zh')

        description_en = post.get('description_en')
        description_ar = post.get('description_ar')
        description_fa = post.get('description_fa')
        description_hi = post.get('description_hi')
        description_ru = post.get('description_ru')
        description_zh = post.get('description_zh')

        route_en = post.get('route_en')
        route_ar = post.get('route_ar')
        route_fa = post.get('route_fa')
        route_hi = post.get('route_hi')
        route_ru = post.get('route_ru')
        route_zh = post.get('route_zh')

        duration = post.get('duration')
        if not duration:
            duration = None

        num_people = post.get('num_people')

        if not num_people:
            num_people = None

        guide = post.get('guide')

        price = post.get('price')
        if not price:
            price = None

        icon = post.get('icon')

        t_facilities = post.getlist('t_facilities')

        t_expenses = post.getlist('t_expenses')

        title = {
            'title_en': title_en,
            'title_ar': title_ar,
            'title_fa': title_fa,
            'title_hi': title_hi,
            'title_ru': title_ru,
            'title_zh': title_zh,
        }

        description = {
            'description_en': description_en,
            'description_ar': description_ar,
            'description_fa': description_fa,
            'description_hi': description_hi,
            'description_ru': description_ru,
            'description_zh': description_zh,
        }

        plan = {
            'plan_en': plan_en,
            'plan_ar': plan_ar,
            'plan_fa': plan_fa,
            'plan_hi': plan_hi,
            'plan_ru': plan_ru,
            'plan_zh': plan_zh,
        }

        route = {
            'route_en': route_en,
            'route_ar': route_ar,
            'route_fa': route_fa,
            'route_hi': route_hi,
            'route_ru': route_ru,
            'route_zh': route_zh,
        }

        tour = Tour(title=title, description=description, plan=plan, route=route,
                    duration=duration, num_people=num_people, guide=guide, price=price)
        tour.save()

        for f in t_facilities:
            obj = TourFacility.objects.get(id=f)
            obj.tours.add(tour)
            obj.save()

        for t in t_expenses:
            obj = TourExpense.objects.get(id=t)
            obj.tours.add(tour)
            obj.save()

        images = self.request.FILES.getlist('image')

        for i in images:
            ti = TourImage.objects.create(image=i, tour=tour)
            tour.images.add(ti)
            tour.save()

        tour.save()

        return HttpResponseRedirect(reverse('adminka-tours'))


class ToursUpdateView(View):
    def get(self, request, id):
        tour = Tour.objects.get(id=id)
        t_expenses = TourExpense.objects.all()
        t_facilities = TourFacility.objects.all()
        t_images = TourImage.objects.filter(tour=tour)

        return render(request, 'adminka/tours/tours_update.html',
                      {'tour': tour, 't_expenses': t_expenses, 't_facilities': t_facilities, 't_images': t_images})

    def post(self, request, id):
        tour = Tour.objects.get(id=id)

        post = self.request.POST

        title_en = post.get('title_en')
        title_ar = post.get('title_ar')
        title_fa = post.get('title_fa')
        title_hi = post.get('title_hi')
        title_ru = post.get('title_ru')
        title_zh = post.get('title_zh')

        plan_en = post.get('plan_en')
        plan_ar = post.get('plan_ar')
        plan_fa = post.get('plan_fa')
        plan_hi = post.get('plan_hi')
        plan_ru = post.get('plan_ru')
        plan_zh = post.get('plan_zh')

        description_en = post.get('description_en')
        description_ar = post.get('description_ar')
        description_fa = post.get('description_fa')
        description_hi = post.get('description_hi')
        description_ru = post.get('description_ru')
        description_zh = post.get('description_zh')

        route_en = post.get('route_en')
        route_ar = post.get('route_ar')
        route_fa = post.get('route_fa')
        route_hi = post.get('route_hi')
        route_ru = post.get('route_ru')
        route_zh = post.get('route_zh')

        duration = post.get('duration')
        if not duration:
            duration = None

        num_people = post.get('num_people')

        if not num_people:
            num_people = None

        guide = post.get('guide')

        price = post.get('price')

        if not price:
            price = None

        title = {
            'title_en': title_en,
            'title_ar': title_ar,
            'title_fa': title_fa,
            'title_hi': title_hi,
            'title_ru': title_ru,
            'title_zh': title_zh,
        }

        description = {
            'description_en': description_en,
            'description_ar': description_ar,
            'description_fa': description_fa,
            'description_hi': description_hi,
            'description_ru': description_ru,
            'description_zh': description_zh,
        }

        plan = {
            'plan_en': plan_en,
            'plan_ar': plan_ar,
            'plan_fa': plan_fa,
            'plan_hi': plan_hi,
            'plan_ru': plan_ru,
            'plan_zh': plan_zh,
        }

        route = {
            'route_en': route_en,
            'route_ar': route_ar,
            'route_fa': route_fa,
            'route_hi': route_hi,
            'route_ru': route_ru,
            'route_zh': route_zh,
        }

        images = self.request.FILES.getlist('image')

        for i in images:
            ti, _ = TourImage.objects.get_or_create(image=i, tour=tour)
            tour.images.add(ti)

        t_facilities = post.getlist('t_facilities')
        t_expenses = post.getlist('t_expenses')

        tour.t_facilities.clear()
        for f in t_facilities:
            obj = TourFacility.objects.get(id=f)
            obj.tours.add(tour)
            obj.save()

        tour.t_expenses.clear()
        for e in t_expenses:
            obj = TourExpense.objects.get(id=e)
            obj.tours.add(tour)
            obj.save()

        tour.title = title
        tour.description = description
        tour.plan = plan
        tour.route = route
        tour.duration = duration
        tour.num_people = num_people
        tour.guide = guide
        tour.price = price

        tour.save()

        return HttpResponseRedirect(reverse('adminka-tours'))


@csrf_exempt
def tour_image_delete(self):
    image = TourImage.objects.get(id=self.POST.get('key'))
    image.image.delete()
    image.delete()
    return HttpResponse('image deleted')


class ToursDeleteView(View):
    def get(self, request, id):
        tour = Tour.objects.get(id=id)
        tour.delete()
        return HttpResponseRedirect(reverse('adminka-tours'))


class AdminToursExpensesView(View):
    def get(self, request):
        if request.GET.get('q'):
            search_term = request.GET.get('q')
            if request.LANGUAGE_CODE == 'en':
                search_result = TourExpense.objects.all().filter(title__title_en__icontains=search_term)
            else:
                search_result = TourExpense.objects.all().filter(title__title_ru__icontains=search_term)

            return render(request, 'adminka/tours/tour_expenses.html', {'t_expenses': search_result})

        t_expenses = TourExpense.objects.all()
        page = request.GET.get('page', 1)

        paginator = Paginator(t_expenses, 15)
        try:
            t_expenses = paginator.page(page)
        except PageNotAnInteger:
            t_expenses = paginator.page(1)
        except EmptyPage:
            t_expenses = paginator.page(paginator.num_pages)

        return render(request, 'adminka/tours/tour_expenses.html', {'t_expenses': t_expenses})


class AdminToursExpensesCreateView(View):
    def get(self, request):
        return render(request, 'adminka/tours/tour_expenses_create.html', {'icons_list': my_tuple})

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

        # image = self.request.FILES.get('image')
        icon = post.get('icon')

        TourExpense.objects.create(title=title, icon=icon)

        return HttpResponseRedirect(reverse('tour-expenses'))


class AdminToursExpensesUpdateView(View):
    def get(self, request, id):
        t_expense = TourExpense.objects.get(id=id)
        if t_expense.get_icon_display():
            icons_listt = list(my_tuple)
            icons_listt.remove(icons_listt[t_expense.icon])
        else:

            icons_listt = list(my_tuple)
        return render(request, 'adminka/tours/tour_expenses_update.html', {'t_expense': t_expense,
                                                                           'icons_listt': icons_listt})

    def post(self, request, id):
        t_expense = TourExpense.objects.get(id=id)
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

        # image = self.request.FILES.get('image')

        icon = post.get('icon')

        t_expense.title = title
        t_expense.icon = icon

        t_expense.save()
        return HttpResponseRedirect(reverse('tour-expenses'))


class AdminToursExpensesDeleteView(View):
    def get(self, request, id):
        t = TourExpense.objects.get(id=id)
        t.delete()
        return HttpResponseRedirect(reverse('tour-expenses'))


class AdminToursFacilitiesView(View):
    def get(self, request):
        if request.GET.get('q'):
            search_term = request.GET.get('q')
            if request.LANGUAGE_CODE == 'en':
                search_result = TourFacility.objects.all().filter(title__title_en__icontains=search_term)
            else:
                search_result = TourFacility.objects.all().filter(title__title_ru__icontains=search_term)

            return render(request, 'adminka/tours/tour_facilities.html', {'t_facilities': search_result})

        t_facilities = TourFacility.objects.all()

        page = request.GET.get('page', 1)

        paginator = Paginator(t_facilities, 15)
        try:
            t_facilities = paginator.page(page)
        except PageNotAnInteger:
            t_facilities = paginator.page(1)
        except EmptyPage:
            t_facilities = paginator.page(paginator.num_pages)

        return render(request, 'adminka/tours/tour_facilities.html', {'t_facilities': t_facilities})


class AdminToursFacilitiesCreateView(View):
    def get(self, request):
        return render(request, 'adminka/tours/tour_facilities_create.html', {'icons_list': my_tuple})

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

        # image = self.request.FILES.get('image')

        icon = post.get('icon')

        TourFacility.objects.create(title=title, icon=icon)

        return HttpResponseRedirect(reverse('tour-facilities'))


class AdminToursFacilitiesUpdateView(View):
    def get(self, request, id):
        t_facility = TourFacility.objects.get(id=id)
        if t_facility.get_icon_display():
            icons_listt = list(my_tuple)
            icons_listt.remove(icons_listt[t_facility.icon])
        else:
            icons_listt = list(my_tuple)
        return render(request, 'adminka/tours/tour_facilities_update.html', {'t_facility': t_facility,
                                                                             'icons_listt': icons_listt})

    def post(self, request, id):
        t_facility = TourFacility.objects.get(id=id)
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

        # image = self.request.FILES.get('image')

        icon = post.get('icon')

        t_facility.title = title
        t_facility.icon = icon

        t_facility.save()
        return HttpResponseRedirect(reverse('tour-facilities'))


class AdminToursFacilitiesDeleteView(View):
    def get(self, request, id):
        t = TourFacility.objects.get(id=id)
        t.delete()
        return HttpResponseRedirect(reverse('tour-facilities'))
