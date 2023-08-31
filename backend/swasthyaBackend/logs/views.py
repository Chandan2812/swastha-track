from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import UserWorkoutLog, UserNutritionLog
from .serializers import UserWorkoutLogSerializer, UserNutritionLogSerializer

class UserWorkoutLogListCreate(generics.ListCreateAPIView):
    queryset = UserWorkoutLog.objects.all()
    serializer_class = UserWorkoutLogSerializer

class UserNutritionLogListCreate(generics.ListCreateAPIView):
    queryset = UserNutritionLog.objects.all()
    serializer_class = UserNutritionLogSerializer
