from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserProfileListCreate.as_view(), name='user-list-create'),
    path('fitness-goals/', views.FitnessGoalListCreate.as_view(), name='fitness-goals-listcreate'),
    path('progress-tracking/', views.ProgressTrackingListCreate.as_view(), name='progress-tracking-listcreate'),
]

