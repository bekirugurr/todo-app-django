from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

#! List and add view
def home(request):
    form = TodoForm()
    todos = Todo.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {
        'form' : form,
        'todos' : todos
    }
    return render(request, 'todo/home.html', context) 

def update(request, id):
    todo = Todo.objects.get(id=id)
    is_done = todo.is_done
    form = TodoForm(instance=todo)
    todos = Todo.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid:
            form.save()
            todo = Todo.objects.get(id=id)
            todo.is_done = is_done
            todo.save()
            return redirect('home')
    context = {
        'form' : form,
        'todos' : todos
    }
    return render(request, 'todo/home.html', context) 

def change_is_done(request, id):
    todo = Todo.objects.get(id=id)
    if todo.is_done == False:
        todo.is_done = True 
    else:
        todo.is_done = False
    todo.save()
    return redirect('home')

def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('home')
