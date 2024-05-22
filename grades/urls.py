from django.urls import path
from . import views

urlpatterns = [
    path('student_grades/', views.student_list, name='student_grades'),
]