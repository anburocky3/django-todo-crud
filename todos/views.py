from django.shortcuts import render
from django.http import HttpResponse

from .models import Todos

# Create your views here.
def index(request):
    todoLists = Todos.objects.all()

    context = {
        'title' : 'Webpy',
        'lists' : todoLists
    }
    return render(request, "todos/index.html", context)

def about(request):
    return render(request, "todos/about.html")


def task_detail(request, id):
    Todolist = Todos.objects.get(id=id)

    context = {
        'title': Todolist.title,
        'list': Todolist
    }

    return render(request, "todos/details.html", context)
