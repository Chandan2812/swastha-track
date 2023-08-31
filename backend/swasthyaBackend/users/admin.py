from django.contrib import admin

# Register your models here.
from .models import UserProfile

admin.site.register(UserProfile)


from .models import FitnessGoal, ProgressTracking

admin.site.register(FitnessGoal)
admin.site.register(ProgressTracking)
