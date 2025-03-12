from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)    # default model
    
    
    # additional fields(custom models)
    address=models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=100)
    img=models.ImageField(upload_to='userimg/',null=True,blank=True)



    