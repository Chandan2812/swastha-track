from django.db import models

# Create your models here.


class TrainerProfile(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
    
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    specialization = models.CharField(max_length=255)
    experience = models.PositiveIntegerField()  # years of experience
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return self.name
