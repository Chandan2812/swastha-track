from django.db import models

# Create your models here.

from plans.models import WorkoutPlan

class UserWorkoutLog(models.Model):
    date = models.DateField()
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    exercises = models.TextField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")


from plans.models import NutritionPlan

class UserNutritionLog(models.Model):
    date = models.DateField()
    nutrition_plan = models.ForeignKey(NutritionPlan, on_delete=models.CASCADE)
    meals = models.TextField()
    caloric_intake = models.PositiveIntegerField(help_text="Calories consumed")
