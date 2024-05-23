from django.urls import path
from grades import views
app_name = 'grades'

urlpatterns = [
    path('list/', views.student_list, name='list'),
]