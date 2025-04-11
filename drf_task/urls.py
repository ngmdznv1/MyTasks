from django.urls import path
from .views import *

urlpatterns = [
  path('api/v1/tasks/', task_list)
]