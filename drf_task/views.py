from django.shortcuts import render
from MyTasks.models import Task
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from rest_framework.response import Response
from .serializers import TaskSerializers


# Create your views here.

# def task_list(request):
#     return HttpResponse('Мой новый проект')

@api_view()
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializers(tasks, many=True)
    return Response(serializer.data)
