from django.urls import path
from .views import DegreeDetailView
from . import views

urlpatterns = [
    path('', views.home, name='polls-home'),
    path('degrees/', views.degrees, name='polls-degrees'),
    path('teachers-ranking/', views.teachers_ranking, name='teachers-ranking'),
    path('subjects-ranking/', views.subjects_ranking, name='subjects-ranking'),
    path('degree/<int:pk>/', DegreeDetailView.as_view, name='degree_info'),
]
