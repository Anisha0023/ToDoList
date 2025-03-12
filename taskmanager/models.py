from django.db import models
# from django_recaptcha.fields import ReCaptchaField

# Create your models here.
class Task(models.Model):
    task_id=models.CharField(max_length=100)
    task_name=models.CharField(max_length=100)
    assigned_by=models.CharField(max_length=100)
    assigned_to=models.CharField(max_length=100)
    description=models.TextField()
    assigned_date=models.DateField(auto_now_add=True)
    priority=models.CharField(max_length=100)
    status=models.CharField(max_length=100,null=True, blank=True)
    # screenshots = models.ImageField(upload_to='screenshots/', null=True, blank=True)

    def __str__(self):
        return self.task_name
class Images(models.Model):
    image=models.ImageField(upload_to='task_images/')
    task=models.ForeignKey(Task,related_name='screenshots',on_delete=models.CASCADE)
    

    # ,blank=True,null=True


