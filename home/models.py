from django.db import models
from university .validators import image_validation_extension

# Create your models here.
#landing page image models
class Carousel(models.Model):
    heading = models.CharField(max_length=500)
    body = models.TextField()
    image = models.ImageField(upload_to='home/carousel/', validators=[image_validation_extension])
    buttonMessage= models.CharField(max_length=255)


    def get_absolute_url(self):
        return reverse('home:index.html')

    def __str__(self):
        return f"{self.heading}"

#headline circles models
class Headline(models.Model):
    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='home/feautured/',validators=[image_validation_extension])
    content = models.TextField()
    buttonAction = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('home:index.html')

    def __str__(self):
        return f"{self.heading}"

#main content feature article (first one)
class FirstFeautured(models.Model):
    image = models.ImageField(upload_to='home/feautured/',validators=[image_validation_extension])
    heading = models.CharField(max_length=300)
    content = models.TextField()

    def get_absolute_url(self):

        return reverse('home:index.html')

    def __str__(self):
        return f"{self.heading}"

#main content feature article (second one)
class SecondFeautured(models.Model):
    image = models.ImageField(upload_to='home/feautured/',validators=[image_validation_extension])
    heading = models.CharField(max_length=300)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('home:index.html')

    def __str__(self):
        return f"{self.heading}"

#main content feature article (third one)
class ThirdFeautured(models.Model):
    image = models.ImageField(upload_to='home/feautured/',validators=[image_validation_extension])
    heading = models.CharField(max_length=300)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('home:index.html')

    def __str__(self):
        return f"{self.heading}"

