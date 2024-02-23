from django.core import exceptions
from django.core.paginator import Paginator

from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from AlbumApp_Django.web.forms import ProfileCreateForm, ProfileDeleteForm
from AlbumApp_Django.web.models import Profile, Album
from django.views import generic as views


class IndexView(views.CreateView):
    template_name = 'core/home-no-profile.html'  # Default template for the index view
    model = Profile
    form_class = ProfileCreateForm

    def get_template_names(self):
        # Check if any profiles exist
        if Profile.objects.exists():
            # If profiles exist, switch to the template with profile
            return ['core/home-with-profile.html']
        else:
            # If no profiles exist, use the default template
            return [self.template_name]

    def get_success_url(self):
        return reverse('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProfileCreateForm()
        context['profile'] = Profile.objects.first()

        # Paginate the queryset of albums
        albums_queryset = Album.objects.all()
        paginator = Paginator(albums_queryset, per_page=1)  # Change per_page as needed
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['albums'] = page_obj  # Pass the paginated queryset to the context

        return context



class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        profile =Profile.objects.first()
        return profile

class DeleteProfileView(views.DeleteView):
    model = Profile
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('index')
    def get_object(self, queryset=None):
        profile =Profile.objects.first()
        return profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProfileDeleteForm()
        return context

