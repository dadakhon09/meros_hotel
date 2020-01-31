from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt

from adminka.model.room import Room, RoomImage


class AdminRoomsView(View):
    def get(self, request):
        if request.GET.get('q'):
            search_term = request.GET.get('q')
            if request.LANGUAGE_CODE == 'en':
                search_result = Room.objects.all().filter(title__title_en__icontains=search_term)
            else:
                search_result = Room.objects.all().filter(title__title_ru__icontains=search_term)

            return render(request, 'adminka/rooms/rooms.html', {'rooms': search_result})

        rooms = Room.objects.all()

        page = request.GET.get('page', 1)

        paginator = Paginator(rooms, 15)
        try:
            rooms = paginator.page(page)
        except PageNotAnInteger:
            rooms = paginator.page(1)
        except EmptyPage:
            rooms = paginator.page(paginator.num_pages)

        return render(request, 'adminka/rooms/rooms.html', {'rooms': rooms})


class RoomsCreateView(View):
    def get(self, request):
        return render(request, 'adminka/rooms/rooms_create.html')

    def post(self, request):
        post = self.request.POST

        title_en = post.get('title_en')
        title_ru = post.get('title_ru')

        title = {
            'title_en': title_en,
            'title_ru': title_ru
        }

        description_en = post.get('description_en')
        description_ru = post.get('description_ru')

        description = {
            'description_en': description_en,
            'description_ru': description_ru
        }

        room_type = post.get('room_type')

        price = post.get('price')
        if not price:
            price = None

        square_meter = post.get('square_meter')
        if not square_meter:
            square_meter = None

        images = self.request.FILES.getlist('image')

        room = Room.objects.create(title=title, description=description, room_type=room_type,
                                     price=price, square_meter=square_meter)

        room.save()

        for i in images:
            RoomImage.objects.create(image=i, room=room)

        return HttpResponseRedirect(reverse('adminka-rooms'))


class RoomsUpdateView(View):
    def get(self, request, id):
        room = Room.objects.get(id=id)
        r_images = RoomImage.objects.filter(room=room)
        return render(request, 'adminka/rooms/rooms_update.html',
                      {'room': room, 'r_images': r_images})

    def post(self, request, id):
        room = Room.objects.get(id=id)

        post = self.request.POST

        title_en = post.get('title_en')
        title_ru = post.get('title_ru')

        title = {
            'title_en': title_en,
            'title_ru': title_ru,
        }
        description_en = post.get('description_en')
        description_ru = post.get('description_ru')

        description = {
            'description_en': description_en,
            'description_ru': description_ru,
        }

        room_type = post.get('room_type')

        images = self.request.FILES.getlist('image')

        price = post.get('price')
        if not price:
            price = None

        square_meter = post.get('square_meter')
        if not square_meter:
            square_meter = None

        room.title = title
        room.description = description
        room.room_type = room_type
        room.price = price
        room.square_meter = square_meter

        room.save()

        for i in images:
            ri, _ = RoomImage.objects.get_or_create(image=i, room=room)

        return HttpResponseRedirect(reverse('adminka-rooms'))


class RoomsDeleteView(View):
    def get(self, request, id):
        r = Room.objects.get(id=id)
        r.delete()
        return HttpResponseRedirect(reverse('adminka-rooms'))


@csrf_exempt
def room_image_delete(self):
    image = RoomImage.objects.get(id=self.POST.get('key'))
    image.image.delete()
    image.delete()
    return HttpResponse('image deleted')
