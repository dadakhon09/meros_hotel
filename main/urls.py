from django.urls import path

from main.about.views import AboutView
from main.contact.views import ContactView
from main.gallery.views import GalleryView
from main.core.views import IndexView
from main.rooms.views import RoomsView, RoomView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('accommodation/', RoomsView.as_view(), name='rooms'),
    path('accommodation/<str:slug>/', RoomView.as_view(), name='room-view'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
]

