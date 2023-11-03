from django.contrib import admin

from motorcycle.blog.models import Blog, BlogImage, BlogMoreInformation


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_of_creation')
    list_filter = ('date_of_creation',)


@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    ...


@admin.register(BlogMoreInformation)
class BlogMoreInformationAdmin(admin.ModelAdmin):
    list_display = ('blog', 'date_of_creation')
    list_filter = ('date_of_creation',)