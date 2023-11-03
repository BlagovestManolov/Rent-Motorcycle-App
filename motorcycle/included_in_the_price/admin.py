from django.contrib import admin

from motorcycle.included_in_the_price.models import IncludedInThePrice


@admin.register(IncludedInThePrice)
class IncludedInThePriceAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_creation')
    list_filter = ('date_of_creation',)