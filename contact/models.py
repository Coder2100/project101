from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message = models.TextField()
    #asked_date = models.TimeField(auto_now=True)
    posted_date  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.email}, {self.subject}, {self.message}, {self.posted_date}"

   #response to user questions     
class Answer(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"{self.question}, {self.answer}"