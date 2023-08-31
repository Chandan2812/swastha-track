from django.db import models

# Create your models here.

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name
