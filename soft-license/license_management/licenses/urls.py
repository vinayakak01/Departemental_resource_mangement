from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('operating_systems/', views.manage_operating_systems, name='manage_operating_systems'),
    path('operating_systems/edit/<int:id>/', views.edit_operating_system, name='edit_operating_system'),
    path('operating_systems/delete/<int:id>/', views.delete_operating_system, name='delete_operating_system'),
    path('ides/', views.manage_ides, name='manage_ides'),
    path('ides/edit/<int:id>/', views.edit_ide, name='edit_ide'),
    path('ides/delete/<int:id>/', views.delete_ide, name='delete_ide'),
    path('softwares/', views.manage_softwares, name='manage_softwares'),
    path('softwares/edit/<int:id>/', views.edit_software, name='edit_software'),
    path('softwares/delete/<int:id>/', views.delete_software, name='delete_software'),
]
