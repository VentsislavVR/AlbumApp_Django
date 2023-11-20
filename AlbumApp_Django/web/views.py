from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'core/home-with-profile.html')


def details_album(request, pk):
    return render(request, 'albums/album-details.html')


def add_album(request):
    return render(request, 'albums/add-album.html')


def edit_album(request, pk):
    return render(request, 'albums/edit-album.html')


def delete_album(request, pk):
    return render(request, 'albums/delete-album.html')


def details_profile(request):
    return render(request, 'profiles/profile-details.html')


def delete_profile(request):
    return render(request, 'profiles/profile-delete.html')
