from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .models import Todo


class IndexView(generic.ListView):
    model = Todo


def add(request):
    if request.method == 'GET':
        return render(request, 'todo/add.html')
    else:
        todo_text = request.POST['todo_text']
        todo_date = request.POST['todo_date']
        new_todo = Todo(todo_text=todo_text, todo_date=todo_date)
        new_todo.save()
        return HttpResponseRedirect(reverse('index'))