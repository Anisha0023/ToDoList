from django.shortcuts import render,redirect
from registerapp.forms import UserForm,UserprofileForm,UpdateForm,UserprofileUpdateForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    registered=False
    if request.method == 'POST':
        # collecting the data from form
        form=UserForm(request.POST)
        form2=UserprofileForm(request.POST,request.FILES)  # request.FILES bcz it is accepting images
        if form.is_valid() and form2.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()

            profile=form2.save(commit=False)    # combining both model field
            profile.user=user     
            profile.save()
            registered=True
            print("validation successfull")
            print(form.cleaned_data['username'])
            print(form.cleaned_data['password'])
            print(form2.cleaned_data['address'])
    else:
        form=UserForm()
        form2=UserprofileForm()

    context={
        'form':form,
        'form2':form2,
        'registered':registered
    }
    # return render(request,'registration.html',{'form':form,'form2':form2})
    return render(request,'registration.html',context)

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        print(password)
        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse("<h1> user is not active</h1>")
        else:
            return HttpResponse("<h1> please check your credentials</h1>")


    return render(request,'login.html',{})

@login_required(login_url='login')
def home(request):
    return render(request,'home.html',{})

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard.html',{})

@login_required(login_url='login')
def update(request):
    if request.method == "POST":
        form = UpdateForm(request.POST, instance=request.user)
        form1=UserprofileUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)
        if form.is_valid() and form1.is_valid():
            user = form.save()
            user.save()

            profile=form1.save(commit=False)    # combining both model field
            profile.user=user     
            profile.save()
            return redirect('dashboard')
    else:
        form = UpdateForm(instance=request.user)  # Initialize the form for GET requests or invalid POST cases
        form1=UserprofileUpdateForm(instance=request.user.userprofile)
    context={
        'form':form,
        'form1':form1,
    }
    return render(request, 'update.html', context)
