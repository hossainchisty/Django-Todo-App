from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.
def home(request):
    tasks = Task.objects.all()

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save() 
        return redirect('/')

    context = {'form':form, 'tasks':tasks}

    return render(request, 'index.html', context)

def update_tasks(request, pk):
        task = Task.objects.get(id=pk)
        form = TaskForm(instance=task)

        if request.method == 'POST':
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save() 
            return redirect('/')
        
        context = {'form':form}
        return render(request, 'update_tasks.html', context)

def delete_tasks(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect('/')
        
    context = {'item':item}

    return render(request, 'delete_tasks.html', context)