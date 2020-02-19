from django.urls import path

from main.about.views import AboutView
from main.contact.views import ContactView
from main.gallery.views import GalleryView
from main.core.views import IndexView
from main.rooms.views import RoomsView, RoomView, AvailableRoomsView, CheckAvailability, BookView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('check_availability/', CheckAvailability.as_view(), name='check_availability'),
    path('book/<int:room_id>/', BookView.as_view(), name='book'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('accommodation/', RoomsView.as_view(), name='rooms'),
    path('available/', AvailableRoomsView.as_view(), name='available-rooms'),
    path('accommodation/<str:slug>/', RoomView.as_view(), name='room-view'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
]

