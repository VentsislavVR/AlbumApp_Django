
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('AlbumApp_Django.web.urls')),
    path('albums/',include('AlbumApp_Django.albums.urls')),
]
