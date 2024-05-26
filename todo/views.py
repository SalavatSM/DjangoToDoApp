from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    return render(request, 'todo/index.html', {'tasks': tasks, 'form': form})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')


def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.complete = True
    task.save()
    return redirect('index')


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('index')

