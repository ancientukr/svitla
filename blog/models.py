from django.db import models

# Create your models here.

class Post(models.Model):
    #image_save_url = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"static/images/album_cover")

    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=500)
    data = models.DateField(auto_now=True)
    cover = models.ImageField(upload_to="media")
    text = models.CharField(max_length=10000)

    def __str__ (self):
        return self.name
