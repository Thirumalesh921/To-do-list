from django.shortcuts import render, redirect
from .models import tasks
from django.contrib.auth.models import User,auth

def todo_list(request):
    current_user = request.user
    user_id = current_user.id
    if user_id is None:
        return render(request, 'index.html')
    list_task = tasks.objects.filter(p_id=user_id)
    return render(request, 'index.html', {'tasks': list_task})

def actions(request):
    if request.method=='POST':
        action=request.POST.get('action')
        if '+' in action:
            s=action.split('+')
            action=s[0]
            task_id=int(s[1])
        if action=='add':
            task_text=request.POST.get('task_text')
            if task_text:
                tasks.objects.create(p_id=request.user.id,test=task_text)
        elif action=='toggle':
            t=tasks.objects.get(id=task_id)
            t.isdone=not t.isdone
            t.save()
        elif action=='delete':
            tasks.objects.filter(id=task_id).delete()
    return redirect('todo_list')