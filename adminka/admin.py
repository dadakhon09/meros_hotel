from django.contrib import admin

from adminka.models import SightCategory, TourFacility, TourExpense, Tour, Sight, Villa, News, \
    VillaServiceCategory, VillaService, About, TourImage, VillaImage, AboutImage, Car, CarImage, SightImage

admin.site.register(SightCategory)
admin.site.register(TourFacility)
admin.site.register(TourExpense)
admin.site.register(Tour)
admin.site.register(TourImage)
admin.site.register(VillaServiceCategory)
admin.site.register(VillaService)
admin.site.register(Sight)
admin.site.register(SightImage)
admin.site.register(Villa)
admin.site.register(VillaImage)
admin.site.register(News)
admin.site.register(About)
admin.site.register(AboutImage)
admin.site.register(Car)
admin.site.register(CarImage)
