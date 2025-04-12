from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/tasks/', views.task_list),
    path('api/v1/tasks/<int:pk>/', views.task_detail),
    path('api/v1/tasks/create/', views.task_create),
    path('api/v1/tasks/<int:pk>/update/', views.task_update),
    path('api/v1/tasks/<int:pk>/delete/', views.task_delete),
    path('api/v1/register/', views.register_user),
    path('api/v1/login/', views.login_user),
]
