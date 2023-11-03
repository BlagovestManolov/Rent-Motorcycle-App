from django.contrib import admin

from motorcycle.faq.models import DepositAndInsurance, Condition


@admin.register(DepositAndInsurance)
class DepositAndInsuranceAdmin(admin.ModelAdmin):
    list_display = ('question', 'date_of_creation')
    list_filter = ('date_of_creation',)

@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ('question', 'date_of_creation')
    list_filter = ('date_of_creation',)