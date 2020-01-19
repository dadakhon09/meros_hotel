from django.urls import path

from adminka.about.views import AdminAboutView, about_image_delete
from adminka.core.views import AdminIndexView
from adminka.rooms.views import room_image_delete, RoomsDeleteView, RoomsUpdateView, RoomsCreateView, AdminRoomsView
from adminka.users.views import AdminLoginView, ProfileView, AdminLogoutView, ProfileUpdateView

urlpatterns = [
    path('', AdminIndexView.as_view(), name='adminka-index'),

    path('about/', AdminAboutView.as_view(), name='adminka-about'),
    path('about/image/delete/', about_image_delete, name='about-image-delete'),

    path('rooms/', AdminRoomsView.as_view(), name='adminka-rooms'),
    path('rooms/image/delete/', room_image_delete, name='room-image-delete'),
    path('rooms/create/', RoomsCreateView.as_view(), name='rooms-create'),
    path('rooms/update/<int:id>/', RoomsUpdateView.as_view(), name='rooms-update'),
    path('rooms/delete/<int:id>/', RoomsDeleteView.as_view(), name='rooms-delete'),

    path('login/', AdminLoginView.as_view(), name='adminka-login'),
    path('profile/', ProfileView.as_view(), name='adminka-profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('logout/', AdminLogoutView.as_view(), name='adminka-logout'),
]
