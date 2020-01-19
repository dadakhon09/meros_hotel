from django.urls import path

from main.others.views import IndexView, AboutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    # path('rooms/', RoomsView.as_view(), name='rooms'),
    # path('rooms/<str:slug>/', RoomView.as_view(), name='villa-view'),
]
