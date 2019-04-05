from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('company/', include('company.urls')),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('student/', include('student.urls'))
]