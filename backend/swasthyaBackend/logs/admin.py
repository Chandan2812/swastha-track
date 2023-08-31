from django.contrib import admin

# Register your models here.
from .models import UserWorkoutLog, UserNutritionLog

admin.site.register(UserWorkoutLog)
admin.site.register(UserNutritionLog)
