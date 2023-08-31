from django.urls import path
from . import views

urlpatterns = [
    path('trainers/', views.TrainerProfileListCreate.as_view(), name='trainer-list-create'),
]
