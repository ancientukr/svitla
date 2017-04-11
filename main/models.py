import os

from django.db import models


# -*- coding: utf-8 -*-
class Album(models.Model):

    CATEGORIES_PHOTO_ALBUM = (
        ("Wedding", "Свадьба"),
        ("Portrait", "Портрет"),
        ("Family-photo", "Семейное фото"),
        ("Love-Story", "Love Story")
    )
    #image_save_url = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"static/images/album_cover")





    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=500)
    data = models.DateField(auto_now=True)

    location = models.CharField(max_length=100)
    categories = models.CharField(max_length=20, choices=CATEGORIES_PHOTO_ALBUM, default="Свадьба")
    cover = models.ImageField(upload_to="media")

    def __str__ (self):
        return self.name



class Foto(models.Model):

    album = models.ForeignKey(Album)
    photo = models.ImageField(upload_to=self.album.name)
    horizontal = models.BooleanField(default=False)

    def __str__ (self):
        return u'%s/%s' % (self.album.name, self.id)

class Recall(models.Model):
    CATEGORIES_PHOTO_TYPE = (
        ("Wedding", "свадебная"),
        ("Pregnancy", "беременность"),
        ("Family-photo", "семейная/детская"),
        ("Love-Story", "love story"),
        ("Other", "другая")
    )
    name = models.CharField(max_length=30)
    email = models.EmailField()
    social = models.URLField()
    type_photo = models.CharField(max_length=20, choices=CATEGORIES_PHOTO_TYPE, default='свадебная')
    location = models.CharField(max_length=30)
    massage = models.CharField(max_length=1000)
    info_about_my = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class SliderPhoto(models.Model):
    photo = models.ImageField(upload_to='slider')


