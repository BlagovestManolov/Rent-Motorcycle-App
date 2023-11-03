from django.contrib import admin

from motorcycle.about_us.models import AboutUs


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'email')