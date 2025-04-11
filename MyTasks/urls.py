from django.urls import path
from django.views import View

from .views import *

urlpatterns = [
    path('', user_login_view, name='login'),
    path('main/', index, name='main'),
    path('logout/', logout_view, name='logout'),
    path('registration/', registration_view, name='register'),
    path('task/<int:task_id>/mark_completed/', mark_task_completed, name='mark_task_completed'),
    path('task/<int:task_id>/delete/', delete_task, name='delete_task'),
    path('add_task/', add_new_task, name='add_task'),
    path('search/', SearchContent.as_view(), name='search')
]