from django.urls import path, include

from AlbumApp_Django.web.views import IndexView, ProfileDetailsView, DeleteProfileView

urlpatterns=(
    path('',IndexView.as_view(),name='index'),
    path('profile/',include([
        path('details/',ProfileDetailsView.as_view(),name='details profile'),
        path('delete/',DeleteProfileView.as_view(),name='delete profile')
    ])),
)
