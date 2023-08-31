from rest_framework import serializers
from .models import UserWorkoutLog, UserNutritionLog

class UserWorkoutLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWorkoutLog
        fields = '__all__'

class UserNutritionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNutritionLog
        fields = '__all__'
