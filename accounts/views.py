from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            username=request.POST['username']
            email=request.POST['email']
            if User.objects.filter(username=username).exists():
                messages.info(request,'UserName Already Exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password Does not Match')
            return redirect('register')
        return redirect('')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('')
def forgot(request):
    if request.method=='POST':
        action=request.POST.get('action')
        if action=='verify':
            exist=User.objects.filter(username=request.POST.get('username')).exists()
            if exist:
                return render(request,'forgot.html',{'exist':exist})
            else:
                messages.info(request,'Invalid Username')
                return render(request,'forgot.html')
        else:
            password1=request.POST.get('p1')
            password2=request.POST.get('p2')
            exist=User.objects.filter(username=request.POST.get('username')).exists()
            if exist:
                if password1!=password2:
                    messages.info(request,'Password Does not Match')
                    return render(request,'forgot.html')
                else:
                    username=request.POST.get('username')
                    rec=User.objects.get(username=username)
                    rec.set_password(password1)
                    rec.save()
                    print('Saved new password is',rec.password)
                    return redirect('login')
            else:
                messages.info(request,'Invalid Username')
                return render(request,'forgot.html')
        return redirect('login')
    return render(request,'forgot.html')