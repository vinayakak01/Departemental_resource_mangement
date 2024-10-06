from django.contrib import admin
from django.urls import path
from department import views  # Correct import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
