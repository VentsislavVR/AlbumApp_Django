from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from AlbumApp_Django.albums.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from AlbumApp_Django.web.models import Album
from django.views import generic as views


class AlbumCreateView(views.CreateView):
    model = Album
    form_class = AlbumCreateForm
    template_name = 'albums/add-album.html'
    success_url = reverse_lazy('index')
# Create your views here.
def details_album(request, pk):
    album = (Album.objects.filter(pk=pk)
             .get())

    context = {
        'album': album,
    }
    return render(
        request,
        'albums/album-details.html',
        context,
    )




def edit_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST,instance=album)
        if form.is_valid():

            form.save()
            return redirect('index')
    context = {
        'form': form,
        'album': album,

    }
    return render(
        request,
        'albums/edit-album.html',
        context,
    )


class AlbumDeleteView(views.DeleteView):
    model = Album
    template_name = 'albums/delete-album.html'
    form_class = AlbumDeleteForm
    success_url = reverse_lazy('index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs
