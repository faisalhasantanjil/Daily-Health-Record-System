
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


class HealthInfo(models.Model):
    email = models.CharField(max_length=200, null=True, default='')
    blood_sugar = models.FloatField(null=True)
    blood_pressure = models.CharField(max_length=100, null=True)
    weight = models.FloatField(null=True)
    update_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.email


class FoodInfo(models.Model):
    food_name = models.CharField(max_length=200, null=True, default='')
    food_type = models.CharField(max_length=200, null=True, default='')
    food_quantity = models.CharField(max_length=200, null=True, default='')
    food_unit = models.CharField(max_length=200, null=True, default='')
    calories = models.CharField(max_length=200, null=True, default='')
    update_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.food_name


class DietRecord(models.Model):

    EATINGTIME = (
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Evening snack', 'Evening snack'),
    )

    FOODUNIT = (
        ('gram', 'gram'),
        ('liter', 'liter'),
        ('cup', 'cup'),
        ('piece', 'piece'),
    )

    email = models.CharField(max_length=200, null=True, default='')
    chicken = models.FloatField(null=True, default=0, blank=True)
    chicken_unit = models.CharField(
        max_length=100, null=True, choices=FOODUNIT, blank=True)
    beef = models.FloatField(null=True, default=0, blank=True)
    beef_unit = models.CharField(
        max_length=100, null=True, choices=FOODUNIT, blank=True)
    lantil = models.FloatField(null=True, default=0, blank=True)
    lantil_unit = models.CharField(
        max_length=100, null=True, choices=FOODUNIT, blank=True)
    mutton = models.FloatField(null=True, default=0, blank=True)
    mutton_unit = models.CharField(
        max_length=100, null=True, choices=FOODUNIT, blank=True)
    broccoli = models.FloatField(null=True, default=0, blank=True)
    broccoli_unit = models.CharField(
        max_length=100, null=True, choices=FOODUNIT, blank=True)
    potatoes = models.FloatField(null=True, default=0, blank=True)
    potatoes_unit = models.CharField(
        max_length=100, null=True, choices=FOODUNIT, blank=True)
    corn = models.FloatField(null=True, default=0, blank=True)
    corn_unit = models.CharField(
        max_length=100, null=True, choices=FOODUNIT, blank=True)
    apple = models.FloatField(null=True, default=0, blank=True)
    apple_unit = models.CharField(
        max_length=100, null=True, choices=FOODUNIT, blank=True)
    banana = models.FloatField(null=True, default=0, blank=True)
    banana_unit = models.CharField(
        max_length=100, null=True, choices=FOODUNIT, blank=True)
    orange = models.FloatField(null=True, default=0, blank=True)
    orange_unit = models.CharField(
        max_length=100, null=True, choices=FOODUNIT, blank=True)
    rice = models.FloatField(null=True, default=0, blank=True)
    rice_unit = models.CharField(
        max_length=100, null=True, choices=FOODUNIT, blank=True)
    wheat = models.FloatField(null=True, default=0, blank=True)
    wheat_unit = models.CharField(
        max_length=100, null=True, choices=FOODUNIT, blank=True)
    bread = models.FloatField(null=True, default=0, blank=True)
    bread_unit = models.CharField(
        max_length=100, null=True, choices=FOODUNIT, blank=True)
    fish = models.FloatField(null=True, default=0, blank=True)
    fish_unit = models.CharField(
        max_length=100, null=True, choices=FOODUNIT, blank=True)
    milk = models.FloatField(null=True, default=0, blank=True)
    milk_unit = models.CharField(
        max_length=100, null=True, choices=FOODUNIT, blank=True)
    yogurt = models.FloatField(null=True, default=0, blank=True)
    yogurt_unit = models.CharField(
        max_length=100, null=True, choices=FOODUNIT, blank=True)

    time = models.CharField(max_length=100, null=True, choices=EATINGTIME)
    update_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.email


class ExerciseRecord(models.Model):
    EXERCISETIME = (
        ('min', 'min'),
        ('hour', 'hour')
    )
    email = models.CharField(max_length=200, null=True, default='')

    walking = models.FloatField(null=True, default=0, blank=True)
    walking_unit = models.CharField(
        max_length=100, null=True, choices=EXERCISETIME, default='min')
    walking_distance = models.FloatField(null=True, default=0, blank=True)

    jogging = models.FloatField(null=True, default=0, blank=True)
    jogging_unit = models.CharField(
        max_length=100, null=True, choices=EXERCISETIME, default='min')
    jogging_distance = models.FloatField(null=True, default=0, blank=True)

    running = models.FloatField(null=True, default=0, blank=True)
    running_unit = models.CharField(
        max_length=100, null=True, choices=EXERCISETIME, default='min')
    running_distance = models.FloatField(null=True, default=0, blank=True)

    update_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.email
