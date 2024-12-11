from django.shortcuts import render,redirect

# Create your views here.
from .models import Task

# View Task List
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasklist.html', {'tasks': tasks})

# Add a New Task
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect('task_list')
    return render(request, 'addtask.html')