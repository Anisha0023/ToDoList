from django.urls import path
from taskmanager import views

urlpatterns=[
    path('',views.task,name="task"),
    path('edit/<int:id>',views.edittask,name="edit"),
    path('delete/<int:id>',views.delete_task,name="delete"),
    path('description/<int:id>',views.description,name="description")
]