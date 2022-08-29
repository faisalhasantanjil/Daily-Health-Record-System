from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(UserInformation)
admin.site.register(RecordFile)
admin.site.register(HealthInfo)
admin.site.register(FoodInfo)
admin.site.register(DietRecord)
admin.site.register(ExerciseRecord)
