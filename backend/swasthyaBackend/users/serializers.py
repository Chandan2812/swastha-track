from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'



from .models import FitnessGoal, ProgressTracking

class FitnessGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessGoal
        fields = '__all__'

class ProgressTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressTracking
        fields = '__all__'
