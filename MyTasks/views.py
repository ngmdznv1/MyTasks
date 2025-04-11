from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .forms import LoginForm, RegisterForm, TaskFormAddContent
from .models import *


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    tasks = Task.objects.all()

    if request.method == 'POST' and 'save_task' in request.POST:
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id)

        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date')
        task.save()

        return redirect('main')

    context = {
        'title': 'MyTasks',
        'tasks': tasks,
        'edit_task_id': request.POST.get('edit_task_id')
    }
    return render(request, 'MyTasks/main.html', context)


def user_login_view(request):
    if request.user.is_authenticated:
        return redirect('main')

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect('main')
            else:
                return redirect('login')
    else:
        form = LoginForm()

    context = {
        'title': 'Вход в аккаунт',
        'form': form
    }

    return render(request, 'MyTasks/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

def registration_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    context = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'MyTasks/register.html', context)



def mark_task_completed(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        is_completed = 'completed' in request.POST
        task.is_completed = is_completed
        task.save()

    return redirect('main')


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
    return redirect('main')

def add_new_task(request):
    if request.method == 'POST':
        form = TaskFormAddContent(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(**form.cleaned_data)
            task.save()
            return redirect('main')
    else:
        form = TaskFormAddContent

    context = {
        'title': 'Добавление задачи',
        'form': form
    }
    return render(request, 'MyTasks/add_task.html', context)


class SearchContent(ListView):
    model = Task
    template_name = 'MyTasks/main.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        word = self.request.GET.get('q')
        return Task.objects.filter(title__iregex=word)














