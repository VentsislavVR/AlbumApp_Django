from django import forms

from AlbumApp_Django.web.models import Album
class ReadOnlyTextInput(forms.TextInput):
    def render(self, name, value, attrs=None, renderer=None):
        attrs['readonly'] = 'readonly'
        return super().render(name, value, attrs, renderer)

class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets={
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist Name',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price',
                }
            ),
        }

class AlbumCreateForm(AlbumBaseForm):
    ...
class AlbumEditForm(AlbumBaseForm):
    ...
class AlbumDeleteForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'genre': ReadOnlyTextInput(),
        }



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for field_name, field in self.fields.items():
            field.widget.attrs['readonly'] = True