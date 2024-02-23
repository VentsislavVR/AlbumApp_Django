from django.urls import path, include

from AlbumApp_Django.albums.views import details_album, edit_album, AlbumCreateView, AlbumDeleteView

urlpatterns = (
path('album/',include([
        path('details/<int:pk>/',details_album,name='details album'),
        path('add/',AlbumCreateView.as_view(),name='add album'),
        path('edit/<int:pk>/',edit_album,name='edit album'),
        path('delete/<int:pk>/',AlbumDeleteView.as_view(),name='delete album'),

    ])),

)