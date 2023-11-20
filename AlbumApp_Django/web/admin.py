from django.contrib import admin

from AlbumApp_Django.web.models import Profile, Album


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ...
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    ...