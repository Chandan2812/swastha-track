from django.urls import path
from . import views

urlpatterns = [
    path('workout-plans/', views.WorkoutPlanListCreate.as_view(), name='workout-plan-list-create'),
    path('nutrition-plans/', views.NutritionPlanListCreate.as_view(), name='nutrition-plan-list-create'),
]
