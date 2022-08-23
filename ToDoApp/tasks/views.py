from django.shortcuts import render

def to_do_tasks(request):
    return render(request, 'ToDoApp/tasks.html')
