from django.core import serializers
from django.http import JsonResponse
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
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"

    if is_ajax:
        if request.method == "POST":
            uncomplete_task_id = request.POST.get('uncompleteTaskId')
            complete_task_id = request.POST.get('completeTaskId')
            delete_task_id = request.POST.get('deleteTaskId')
            if delete_task_id:
                delete_task = Tasks.objects.get(id=delete_task_id).delete()
            if complete_task_id:
                complete_task = Tasks.objects.get(id=complete_task_id)
                complete_task.completion = True
                complete_task.save()
            if uncomplete_task_id:
                uncomplete_task = Tasks.objects.get(id=uncomplete_task_id)
                uncomplete_task.completion = False
                uncomplete_task.save()
            updated_tasks = serializers.serialize("xml", Tasks.objects.filter(author=request.user))
            return JsonResponse(updated_tasks, safe=False)


    if request.method == "POST":
        task_data = request.POST.get('task_text')
        if task_data:
            task = Tasks.objects.create(author=request.user, to_do=task_data)
            task.save()
            return redirect('/')

    return render(request, 'ToDoApp/tasks.html', {'tasks': tasks})
