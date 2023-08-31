from django.urls import path
from . import views

urlpatterns = [
    path('workout-logs/', views.UserWorkoutLogListCreate.as_view(), name='workout-logs-listcreate'),
    path('nutrition-logs/', views.UserNutritionLogListCreate.as_view(), name='nutrition-logs-listcreate'),
]
