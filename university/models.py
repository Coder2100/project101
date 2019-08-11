from django.db import models

#import reverse for absolute url
from django.urls import reverse
from .data import PROVINCES ,University_Choices
#import file validation module
from .validators import image_validation_extension

# Create your models here.


class UniversityView(models.Model):
    name = models.CharField(choices=University_Choices, max_length=300)
    logo = models.ImageField(upload_to='university/logo/', validators=[image_validation_extension])
    update = models.DateTimeField(auto_now_add=True)
    province = models.CharField(choices=PROVINCES, max_length=244)
    physical_address = models.TextField()

    def get_absolute_url(self):
        return reverse('university:university.html')

    def __str__(self):
        return f"{self.name}"

        
class Faculty(models.Model):
    name = models.CharField(max_length=255)
    school_or_department = models.CharField(max_length=255)

class Contact(models.Model):
    tel = models.IntegerField()
    emai = models.EmailField()
    website = models.CharField(max_length=255)
class AdmissionRequirement(models.Model):
    subject = models.CharField(max_length=255)
