from django.urls import path

from . import views

urlpatterns = [
    path('Login', views.Login, name='Login'),
    path('Dashboard', views.Dashboard, name='Dashboard'),
    path('register_company', views.register_company, name='register_company'),
    path('register_for_job', views.register_for_job, name='register_for_job')
]