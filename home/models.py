from django.db import models
from university .validators import image_validation_extension

# Create your models here.
class Carousel(models.Model):
    heading = models.CharField(max_length=500)
    body = models.TextField()
    image = models.ImageField(upload_to='university/carousel/', validators=[image_validation_extension])
    buttonMessage= models.CharField(max_length=255)


    def get_absolute_url(self):
        return reverse('home:index.html')

    def __str__(self):
        return f"{self.heading}"

class FirstFeautured(models.Model):
    image = models.ImageField(upload_to='university/feautured/',validators=[image_validation_extension])
    heading = models.CharField(max_length=300)
    content = models.TextField()

    def get_absolute_url(self):

        return reverse('home:index.html')

    def __str__(self):
        return f"{self.heading}"

class SecondFeautured(models.Model):
    image = models.ImageField(upload_to='university/feautured/',validators=[image_validation_extension])
    heading = models.CharField(max_length=300)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('home:index.html')

    def __str__(self):
        return f"{self.heading}"


class ThirdFeautured(models.Model):
    image = models.ImageField(upload_to='university/feautured/',validators=[image_validation_extension])
    heading = models.CharField(max_length=300)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('home:index.html')

    def __str__(self):
        return f"{self.heading}"