from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Task

def home(request):
    incomplete_tasks=Task.objects.all().filter(is_completed=False).order_by('-modified_at')
    complete_tasks=Task.objects.all().filter(is_completed=True).order_by('-modified_at')

    context={
        'incomplete_tasks':incomplete_tasks,
        'complete_tasks':complete_tasks
    }
    return render(request, 'home.html', context)
