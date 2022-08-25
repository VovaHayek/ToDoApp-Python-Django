from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .models import User, Tasks

def loginForm(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            if User.objects.filter(username=username).exists():
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('/')
            else:
                user = User.objects.create_user(username, password)
                login(request, user)
                return redirect('/')
    return render(request, 'includes/loginForm.html')

def to_do_tasks(request):
    tasks = Tasks.objects.filter(author=request.user)
    if request.method == "POST":
        task_data = request.POST.get('task_text')
        if task_data:
            task = Tasks.objects.create(author=request.user, to_do=task_data)
            task.save()
            return redirect('/')
    return render(request, 'ToDoApp/tasks.html', {'tasks': tasks})
