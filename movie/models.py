from django.db import models
import numpy as np

# create your models here
def get_default_array():
  default_arr = np.random.rand(1536)  # Adjust this to your desired default array
  return default_arr.tobytes()

# Create your models here.
class Movie (models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, null= True)
    images = models.ImageField(upload_to = 'movie/images/', default = 'movie/images/default.jpg')
    url = models.URLField(blank=True)
    genre = models.CharField(blank=True, max_length=250)
    year = models.IntegerField(blank=True, null= True)
    emb = models.BinaryField(default=get_default_array())

    def __str__(self): 
        return self.title