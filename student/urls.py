from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register_student', views.register_student, name='register_student'),
    path('edit_student_detail', views.edit_student_detail, name='edit_student_detail'),
]