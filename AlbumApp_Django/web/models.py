from enum import Enum

from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from AlbumApp_Django.web.validators import validate_string_alphanumeric


# Create your models here.
class Profile(models.Model):
    MIN_LEN_USERNAME = 2
    MAX_LEN_USERNAME = 15
    username = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_USERNAME,
        validators=(
            MinLengthValidator(MIN_LEN_USERNAME),
            validate_string_alphanumeric,
        ),
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]
class AlbumGenres(ChoicesEnum):

    POP = 'Pop Music'
    JAZZ = 'Jazz Music'
    RNB = 'R&B Music'
    ROCK = 'Rock Music'
    COUNTRY = 'Country Music'
    DANCE = 'Dance Music'
    HIP_HOP = 'Hip Hop Music'
    OTHER = 'Other'


print(AlbumGenres.choices())
class Album(models.Model):
    MAX_LEN_NAME = 30
    MAX_LEN_ARTIST = 30
    MAX_LEN_GENRE = 30

    album_name = models.CharField(
        unique=True,
        max_length=MAX_LEN_NAME,
        null=False,
        blank=False,
        verbose_name='Album Name',
    )
    artist = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_ARTIST
    )
    genre = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_GENRE,
        choices=AlbumGenres.choices(),
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image = models.URLField(
        null=False,
        blank=False,
        verbose_name= 'Image URL',
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(0.0),
        )
    )
    class Meta:
        ordering = ('pk',)








# Without enums ########
# class Album(models.Model):
#     POP_MUSIC = 'Pop Music'
#     JAZZ_MUSIC_MUSIC = 'Jazz Music'
#     RNB_MUSIC = 'R&B Music'
#     ROCK_MUSIC = 'Rock Music'
#     COUNTRY_MUSIC = 'Country Music'
#     DANCE_MUSIC = 'Dance Music'
#     HIP_HOP_MUSIC = 'Hip Hop Music'
#     OTHER_MUSIC = 'Other'
#
#     MUSICS = (
#         (POP_MUSIC, POP_MUSIC),
#         (JAZZ_MUSIC_MUSIC, JAZZ_MUSIC_MUSIC),
#         (RNB_MUSIC, RNB_MUSIC),
#         (ROCK_MUSIC, ROCK_MUSIC),
#         (COUNTRY_MUSIC, COUNTRY_MUSIC),
#         (DANCE_MUSIC, DANCE_MUSIC),
#         (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
#         (OTHER_MUSIC, OTHER_MUSIC),
#     )
#
#     MAX_LEN_NAME = 30
#     MAX_LEN_ARTIST = 30
#     MAX_LEN_GENRE = 30
#
#     album_name = models.CharField(
#         unique=True,
#         max_length=MAX_LEN_NAME,
#         null=False,
#         blank=False,
#         verbose_name='Album Name',
#     )
#     artist = models.CharField(
#         null=False,
#         blank=False,
#         max_length=MAX_LEN_ARTIST
#     )
#     genre = models.CharField(
#         null=False,
#         blank=False,
#         max_length=MAX_LEN_GENRE,
#         choices=MUSICS
#     )
#     description = models.TextField(
#         null=True,
#         blank=True,
#     )
#     image = models.URLField(
#         null=False,
#         blank=False,
#         verbose_name= 'Image URL',
#     )
#     price = models.FloatField(
#         null=False,
#         blank=False,
#         validators=(
#             MinValueValidator(0.0),
#         )
#     )
#     class Meta:
#         ordering = ('pk',)
