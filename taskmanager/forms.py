from django import forms
from taskmanager.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        # fields=['task_id','task_name','assigned_by','assigned_to','assigned_date','priority']
        fields="__all__"
class EditTaskForm(forms.ModelForm):
    task_id=forms.CharField(disabled=True)
    # for disabling from modifying the input
    assigned_by=forms.CharField(disabled=True)
    class Meta:
        model=Task
        fields=['task_id','task_name','assigned_by','assigned_to','description','priority','status']
class DescriptionForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['description']

