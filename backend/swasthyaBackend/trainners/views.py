from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import TrainerProfile
from .serializers import TrainerProfileSerializer

class TrainerProfileListCreate(generics.ListCreateAPIView):
    queryset = TrainerProfile.objects.all()
    serializer_class = TrainerProfileSerializer
