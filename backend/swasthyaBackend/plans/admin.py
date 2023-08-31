from django.contrib import admin

# Register your models here.
from .models import WorkoutPlan, NutritionPlan

admin.site.register(WorkoutPlan)
admin.site.register(NutritionPlan)
