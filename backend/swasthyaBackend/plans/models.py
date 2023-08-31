from django.db import models

# Create your models here.

from trainers.models import TrainerProfile

class WorkoutPlan(models.Model):
    trainer = models.ForeignKey(TrainerProfile, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=255)
    GOAL_CHOICES = [
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('cardio_fitness', 'Cardio Fitness'),
    ]
    goal = models.CharField(choices=GOAL_CHOICES, max_length=50)
    duration = models.PositiveIntegerField()  # in weeks
    description = models.TextField()


class NutritionPlan(models.Model):
    trainer = models.ForeignKey(TrainerProfile, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=255)
    GOAL_CHOICES = [
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('balanced_diet', 'Balanced Diet'),
    ]
    goal = models.CharField(choices=GOAL_CHOICES, max_length=50)
    duration = models.PositiveIntegerField()  # in weeks
    guidelines = models.TextField()
