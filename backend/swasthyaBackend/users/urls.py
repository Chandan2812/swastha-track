from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserProfileListCreate.as_view(), name='user-list-create'),
]
