from django.db import models

# Create your models here.

class TrainerProfile(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    name = models.CharField(max_length=255)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    specialization = models.CharField(max_length=255)
    experience = models.PositiveIntegerField() # In years, for instance
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name
