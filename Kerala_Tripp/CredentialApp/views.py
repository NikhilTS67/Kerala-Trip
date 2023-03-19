from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        usname=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=usname,password=password)
        if user is not None :
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('CredentialApp:login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def register(request):
    if request.method== 'POST':
        usname = request.POST['Username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword= request.POST['cpassword']
        if password==cpassword :
            if User.objects.filter(username=usname).exists():
                messages.info(request , 'User name already taken')
                return redirect('CredentialApp:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request , 'Email ID already exists')
                return redirect('CredentialApp:register')
            else :
                user = User.objects.create_user(username=usname, email=email, password=password, first_name=fname,
                                                last_name=lname)
                user.save()
                print('User created')
                # messages.info(request, 'User Created')
                return redirect('/')
        else:
            messages.info(request, 'Password Missmatch')
            return redirect('CredentialApp:register')
    return render(request, 'registration.html')
