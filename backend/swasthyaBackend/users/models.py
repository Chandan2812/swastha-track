from django.db import models


class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name



class FitnessGoal(models.Model):
    GOAL_CHOICES = [
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('endurance', 'Endurance')
    ]
    goal_type = models.CharField(choices=GOAL_CHOICES, max_length=50)
    target = models.TextField()
    timeline = models.TextField()


class ProgressTracking(models.Model):
    date = models.DateField()
    weight = models.FloatField(help_text="Weight in kilograms")
    body_measurements = models.TextField()
    notes = models.TextField(blank=True)
