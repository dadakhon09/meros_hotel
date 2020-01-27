from django.urls import path

from main.gallery.views import GalleryView
from main.others.views import IndexView, AboutView
from main.rooms.views import RoomsView, RoomView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('rooms/', RoomsView.as_view(), name='rooms'),
    path('rooms/<str:slug>/', RoomView.as_view(), name='room-view'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
]

