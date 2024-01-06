# biomedic_app/models.py
from django.db import models


class Patient(models.Model):
    patient_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(default=0)
    id_number = models.CharField(max_length=20, default="")
    location = models.CharField(max_length=100, default="")
    hiv_status = models.CharField(max_length=10, choices=[('positive', 'Positive'), ('negative', 'Negative')],
                                  default="")
    hepatitis_status = models.CharField(max_length=10, choices=[('positive', 'Positive'), ('negative', 'Negative')],
                                        default="")
    tb_status = models.CharField(max_length=10, choices=[('positive', 'Positive'), ('negative', 'Negative')],
                                 default="")
    unique_number = models.CharField(max_length=10, unique=True, default="")  # Unique randomly generated number

    # Add other fields as needed


class Medication(models.Model):
    name = models.CharField(max_length=100)
    # Add other medication-related fields


class DosageHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    dosage = models.IntegerField()
    date_taken = models.DateField()
    # Add other dosage history-related fields


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
    objects = None
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    objects = None
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.TextField()

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = None

    def __str__(self):
        return "Post #{self.id} in {self.topic.title}"


class EducationalContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # Add other fields as needed

# Create your models here.
