from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='polls-home'),
    path('degrees/', views.degrees, name='polls-degrees'),
    path('teachers-ranking/', views.teachers_ranking, name='teachers-ranking'),
    path('subjects-ranking/', views.subjects_ranking, name='subjects-ranking'),

]