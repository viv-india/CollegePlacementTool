from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    #path('dashboard', views.dashboard, name='dashboard'),
    path('register_company', views.register_company, name='register_company'),
    path(r'^register_for_job/(?P<c_id>\d+)/$', views.register_for_job, name='register_for_job')
]