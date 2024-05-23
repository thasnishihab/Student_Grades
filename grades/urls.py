from django.contrib import admin
from django.urls import path, include
from grades import views
app_name = 'grades'



urlpatterns = [

    path('list/', views.student_list, name='list'),
]