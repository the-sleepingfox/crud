from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name= 'api_overview'),
    path('api/add-students/', views.add_students, name= 'add-students'),
    path('api/view-students/', views.view_students, name= 'view-students'),
    path('api/update-student/<int:pk>/', views.update_student, name= 'update-student'),
    path('api/delete-student/<int:pk>/', views.delete_student, name= 'delete-student'),
]