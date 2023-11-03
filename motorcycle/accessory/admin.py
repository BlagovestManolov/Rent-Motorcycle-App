from django.contrib import admin

from motorcycle.accessory.models import Accessory, AccessoryImage


@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_day', 'date_of_creation')
    list_filter = ('price_per_day', 'date_of_creation')


@admin.register(AccessoryImage)
class AccessoryImageAdmin(admin.ModelAdmin):
    list_filter = ('accessory__name',)