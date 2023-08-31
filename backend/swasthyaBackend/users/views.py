from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer

class UserProfileListCreate(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


from .models import FitnessGoal, ProgressTracking
from .serializers import FitnessGoalSerializer, ProgressTrackingSerializer

class FitnessGoalListCreate(generics.ListCreateAPIView):
    queryset = FitnessGoal.objects.all()
    serializer_class = FitnessGoalSerializer

class ProgressTrackingListCreate(generics.ListCreateAPIView):
    queryset = ProgressTracking.objects.all()
    serializer_class = ProgressTrackingSerializer
