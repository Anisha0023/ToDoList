from django.shortcuts import render,redirect
from taskmanager.models import Task
from taskmanager.forms import TaskForm,EditTaskForm,DescriptionForm
from django.core.paginator import Paginator

# Create your views here.
def task(request):
    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            add_task=form.save()
            add_task.save()
            return redirect("task")
            # print("task is added")
    else:
        all_task=Task.objects.all()
        # pagination functions
        paginator=Paginator(all_task,5)
        page=request.GET.get('pg')
        all_task=paginator.get_page(page)
        form=TaskForm()
    context={'all_task':all_task,'form':form}
    return render(request,'tasks/alltask.html',context)
def edittask(request,id=0):
    data=Task.objects.get(id=id)
    form=EditTaskForm(instance=data)
    if request.method=='POST':
        form=EditTaskForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('task')
    
    # auto filling the data
    return render(request,'tasks/edit_task.html',{'form':form})
def delete_task(request,id=0):
    data=Task.objects.get(id=id)
    data.delete()
    return redirect('task')
def description(request,id=0):
    data=Task.objects.get(id=id)
    screenshots=data.screenshots.all()
    description_form=DescriptionForm(instance=data)
    return render(request,'tasks/description.html',{'screenshots':screenshots,'form':description_form})
 

    

