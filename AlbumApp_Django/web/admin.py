from django.contrib import admin

from AlbumApp_Django.web.models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ...
