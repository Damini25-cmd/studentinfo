
from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import Marks, State,Student
from .Choices import state_id_choices

# Create your views here.
def register(request):
    if request.method == 'POST':
        #GET FROM VALUE
     first_name = request.POST['first_name']
     last_name = request.POST['last_name']
     username = request.POST['username']
     email = request.POST['email']
     password = request.POST['password']
     password2 = request.POST['password2']

        #checking if passwords match
     if password == password2:
         if User.objects.filter(username=username).exists():
             messages.error(request,'That username is taken')
             return redirect('register')
         else:
             if User.objects.filter(email=email).exists():
                 messages.error(request,'That email is used')
                 return redirect('register')
             else:
                 user = User.objects.create_user(username=username ,password= password, email=email,
                 first_name=first_name, last_name=last_name)
                 user.save()
                 messages.success(request,'you are now registerd and can login')
                 return redirect('login')

        #   auth.login(request,user)
        #   messages.success(request,'you are now logged in')
        #   return redirect('index')        
     else:
        messages.error(request,'Password do not match')
        return redirect('register')
    else:
      

      return render(request,'accounts/register.html')
        
def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username , password=password)

    if user is not None:
      auth.login(request,user)
      messages.success(request,'you are now logged in ')
      return redirect('dashboard')
    else:
      messages.error(request,'invalid credentials')
      return redirect('login')

  else:
        return render(request,'accounts/login.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request,'You are now logged out')
    return redirect('index')

def dashboard(request):
  post = State.objects.all()
  queryset = Marks.objects.all()
  student = Student.objects.all()


  


    #city
  if 'state_and_UTs' in request.GET:
     state_and_UTs = request.GET['state_and_UTs']
     if state_and_UTs:
        post = post.filter(state_and_UTs__iexact=state_and_UTs)

  
  
  context = {
      'posts': post,
      'student': student,
      'queryset' : queryset,
     
    }
    
  return render(request,'accounts/dashboard.html',context)
