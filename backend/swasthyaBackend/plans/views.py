from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import WorkoutPlan, NutritionPlan
from .serializers import WorkoutPlanSerializer, NutritionPlanSerializer

class WorkoutPlanListCreate(generics.ListCreateAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer

class NutritionPlanListCreate(generics.ListCreateAPIView):
    queryset = NutritionPlan.objects.all()
    serializer_class = NutritionPlanSerializer
