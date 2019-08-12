from django.db import models
from university .validators import image_validation_extension
# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=225)
    catchy = models.CharField(max_length=400)
    body = models.TextField()
    #thumbnail = models.ImageField(upload_to='')

#project creators
class Creator(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='about/creators/', validators=[image_validation_extension])
    qualification = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('about:about.html')

    def __str__(self):
        return f"{self.name}"