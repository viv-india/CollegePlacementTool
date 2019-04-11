from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register_student', views.register_student, name='register_student'),
    path('edit_student_detail', views.edit_student_detail, name='edit_student_detail'),
    path('student_skill_edit', views.student_skill_edit, name='student_skill_edit'),
    path('student_dashboard', views.student_dashboard, name='student_dashboard'),
    path('placed_skill_rating', views.placed_skill_rating, name='placed_skill_rating')
]