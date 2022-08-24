
from pickle import TRUE
from django.db import models

# Create your models here.


class UserInformation(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    email = models.CharField(max_length=200, null=True, default='')
    name = models.CharField(max_length=100, null=True)
    age = models.FloatField(null=True)
    gender = models.CharField(max_length=100, null=True, choices=GENDER)
    weight = models.FloatField(null=True)
    height = models.FloatField(null=True)
    registration_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.email


class RecordFile(models.Model):
    TYPEOFRECORD = (
        ('Diagnosis Report', 'Diagnosis Report'),
        ('Prescription', 'Prescription'),
        ('Others', 'Others')
    )
    email = models.CharField(max_length=200, null=True, default='')
    referBy = models.CharField(max_length=100, null=True)
    upload_file = models.FileField()
    typeofrecord = models.CharField(
        max_length=100, null=True, choices=TYPEOFRECORD)
    upload_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.email
