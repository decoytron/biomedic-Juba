from django.db import models


# biomedic_app/models.py
from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    hiv_status = models.CharField(max_length=10)
    # Add other fields as needed

class Medication(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed

class CounselingSession(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    counselor_name = models.CharField(max_length=100)
    # Add other fields as needed

class ForumPost(models.Model):
    topic = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Patient, on_delete=models.CASCADE)
    # Add other fields as needed
class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"Post #{self.id} in {self.topic.title}"

class EducationalContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # Add other fields as needed

# Create your models here.
