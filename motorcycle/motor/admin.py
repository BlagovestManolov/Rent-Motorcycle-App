from django.contrib import admin

from motorcycle.motor.models import Motorcycle, MotorcycleImage, MotorcycleDeposit


@admin.register(Motorcycle)
class MotorcycleAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_creation')
    list_filter = ('name', 'date_of_creation')


@admin.register(MotorcycleImage)
class MotorcycleImageAdmin(admin.ModelAdmin):
    list_filter = ('motorcycle__name',)


@admin.register(MotorcycleDeposit)
class MotorcycleDepositAdmin(admin.ModelAdmin):
    list_display = ('motorcycle', 'deposit', 'date_of_creation')