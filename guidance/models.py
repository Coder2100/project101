from django.db import models
from django.contrib.auth import get_user_model
from university.validators import image_validation_extension
# CREATE global variable user
User = get_user_model()
# Create your models here.


class GuidanceView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   # post = models.ForeignKey('Post', on_delete=models.CASCADE)


class applications_development_career(models.Model):
    career_name = models.CharField(max_length=30)
    description = models.TextField()
    potential_employers = models.CharField(max_length=30)
    picture = models.ImageField(
        upload_to='university/careers/', validators=[image_validation_extension])


class network_communication_career(models.Model):
    career_name = models.CharField(max_length=30)
    description = models.TextField()
    potential_employers = models.CharField(max_length=30)
    picture = models.ImageField(
        upload_to='university/careers/', validators=[image_validation_extension])


class multimedia_career(models.Model):
    career_name = models.CharField(max_length=30)
    description = models.TextField()
    potential_employers = models.CharField(max_length=30)
    picture = models.ImageField(
        upload_to='university/careers/', validators=[image_validation_extension])
        
class Fields_of_study_or_course_name(models.Model):
    course_name = models.CharField(max_length=30)

class minimum_admission_requirement(models.Model):
    course =  models.ForeignKey(Fields_of_study_or_course_name, on_delete=models.CASCADE)
    subject = models.CharField(max_length=30)
    subject_mark = models.IntegerField()
    general_admission_requirement = models.TextField()





