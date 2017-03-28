from django.db import models

class Album(models.Model):

    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=500)
    data = models.DateField(auto_now=True)
    cover = models.ImageField()
    location = models.CharField(max_length=100)

    def __str__ (self):
        return self.name

class Foto(models.Model):

    album = models.ForeignKey(Album)
    photo = models.ImageField()

    def __str__ (self):
        return u'%s/%s' % (self.album.name, self.id)

