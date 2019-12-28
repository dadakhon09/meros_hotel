from django.urls import path

from adminka.car.views import AdminCarsView, CarsCreateView, CarsUpdateView, CarsDeleteView, car_image_delete
from adminka.about.views import AdminAboutView, about_image_delete
from adminka.core.views import AdminIndexView
from adminka.news.views import AdminNewsView, NewsCreateView, NewsUpdateView, NewsDeleteView
from adminka.users.views import AdminLoginView, ProfileView, AdminLogoutView, ProfileUpdateView
from adminka.sights.views import AdminSightsView, SightsCreateView, SightsUpdateView, SightsDeleteView, \
    SightsCategoriesView, SightsCategoriesCreateView, SightsCategoriesUpdateView, SightsCategoriesDeleteView, \
    sight_image_delete
from adminka.tours.views import AdminToursView, ToursCreateView, ToursUpdateView, ToursDeleteView, \
    AdminToursExpensesView, AdminToursFacilitiesView, AdminToursExpensesUpdateView, AdminToursExpensesDeleteView, \
    AdminToursFacilitiesUpdateView, AdminToursFacilitiesDeleteView, AdminToursExpensesCreateView, \
    AdminToursFacilitiesCreateView, tour_image_delete
from adminka.villas.views import AdminVillasView, VillasCreateView, VillasUpdateView, VillasDeleteView, \
    VillaServicesView, VillaServicesCreateView, VillaServicesUpdateView, VillaServicesDeleteView, \
    VillaServiceCategoriesView, VillaServiceCategoriesCreateView, VillaServiceCategoriesUpdateView, \
    VillaServiceCategoriesDeleteView, villa_image_delete

urlpatterns = [
    path('', AdminIndexView.as_view(), name='adminka-index'),

    path('about/', AdminAboutView.as_view(), name='adminka-about'),
    path('about/image/delete/', about_image_delete, name='about-image-delete'),

    path('cars/', AdminCarsView.as_view(), name='adminka-cars'),
    path('cars/image/delete/', car_image_delete, name='car-image-delete'),
    path('cars/create/', CarsCreateView.as_view(), name='cars-create'),
    path('cars/update/<int:id>/', CarsUpdateView.as_view(), name='cars-update'),
    path('cars/delete/<int:id>/', CarsDeleteView.as_view(), name='cars-delete'),

    path('news/', AdminNewsView.as_view(), name='adminka-news'),
    path('news/create/', NewsCreateView.as_view(), name='news-create'),
    path('news/update/<int:id>/', NewsUpdateView.as_view(), name='news-update'),
    path('news/delete/<int:id>/', NewsDeleteView.as_view(), name='news-delete'),

    path('sights/', AdminSightsView.as_view(), name='adminka-sights'),
    path('sights/image/delete/', sight_image_delete, name='sight-image-delete'),
    path('sights/create/', SightsCreateView.as_view(), name='sights-create'),
    path('sights/update/<int:id>/', SightsUpdateView.as_view(), name='sights-update'),
    path('sights/delete/<int:id>/', SightsDeleteView.as_view(), name='sights-delete'),
    path('sight_categories/', SightsCategoriesView.as_view(), name='sight-categories'),
    path('sight_categories/create/', SightsCategoriesCreateView.as_view(), name='sight-categories-create'),
    path('sight_categories/update/<int:id>/', SightsCategoriesUpdateView.as_view(), name='sight-categories-update'),
    path('sight_categories/delete/<int:id>/', SightsCategoriesDeleteView.as_view(), name='sight-categories-delete'),

    path('tours/', AdminToursView.as_view(), name='adminka-tours'),
    path('tours/image/delete/', tour_image_delete, name='tour-image-delete'),
    path('tours/create/', ToursCreateView.as_view(), name='tours-create'),
    path('tours/update/<int:id>/', ToursUpdateView.as_view(), name='tours-update'),
    path('tours/delete/<int:id>/', ToursDeleteView.as_view(), name='tours-delete'),
    path('tour_expenses/', AdminToursExpensesView.as_view(), name='tour-expenses'),
    path('tour_expenses/create/', AdminToursExpensesCreateView.as_view(), name='tour-expenses-create'),
    path('tour_expenses/update/<int:id>/', AdminToursExpensesUpdateView.as_view(), name='tour-expenses-update'),
    path('tour_expenses/delete/<int:id>/', AdminToursExpensesDeleteView.as_view(), name='tour-expenses-delete'),
    path('tour_facilities/', AdminToursFacilitiesView.as_view(), name='tour-facilities'),
    path('tour_facilities/create/', AdminToursFacilitiesCreateView.as_view(), name='tour-facilities-create'),
    path('tour_facilities/update/<int:id>/', AdminToursFacilitiesUpdateView.as_view(), name='tour-facilities-update'),
    path('tour_facilities/delete/<int:id>/', AdminToursFacilitiesDeleteView.as_view(), name='tour-facilities-delete'),

    path('villas/', AdminVillasView.as_view(), name='adminka-villas'),
    path('villas/image/delete/', villa_image_delete, name='villa-image-delete'),
    path('villas/create/', VillasCreateView.as_view(), name='villas-create'),
    path('villas/update/<int:id>/', VillasUpdateView.as_view(), name='villas-update'),
    path('villas/delete/<int:id>/', VillasDeleteView.as_view(), name='villas-delete'),
    path('villa_services/', VillaServicesView.as_view(), name='villa-services'),
    path('villa_services/create/', VillaServicesCreateView.as_view(), name='villa-services-create'),
    path('villa_services/update/<int:id>/', VillaServicesUpdateView.as_view(), name='villa-services-update'),
    path('villa_services/delete/<int:id>/', VillaServicesDeleteView.as_view(), name='villa-services-delete'),
    path('villa_service_categories/', VillaServiceCategoriesView.as_view(), name='villa-service-categories'),
    path('villa_service_categories/create/', VillaServiceCategoriesCreateView.as_view(),
         name='villa-service-categories-create'),
    path('villa_service_categories/update/<int:id>/', VillaServiceCategoriesUpdateView.as_view(),
         name='villa-service-categories-update'),
    path('villa_service_categories/delete/<int:id>/', VillaServiceCategoriesDeleteView.as_view(),
         name='villa-service-categories-delete'),

    path('login/', AdminLoginView.as_view(), name='adminka-login'),
    path('profile/', ProfileView.as_view(), name='adminka-profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('logout/', AdminLogoutView.as_view(), name='adminka-logout'),
]
