from django.contrib import admin

from motorcycle.tour.models import Tour, TourImage, TourMoreInformation


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'date_of_creation')
    list_filter = ('date_of_creation',)

@admin.register(TourImage)
class TourImageAdmin(admin.ModelAdmin):
    ...

@admin.register(TourMoreInformation)
class TourMoreInformationAdmin(admin.ModelAdmin):
    list_display = ('tour',)