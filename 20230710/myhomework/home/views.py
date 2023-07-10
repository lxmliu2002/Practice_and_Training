from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserDetails
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            error_message = "用户名或密码错误"
            return render(request, 'home/login.html', {'error_message': error_message})
    else:
        return render(request, 'home/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        gender = request.POST['gender']
        birth = request.POST['birth']
        email = request.POST['email']
        
        if password != confirm_password:
            error_message = "密码不匹配"
            return render(request, 'home/register.html', {'error_message': error_message})
        
        # 创建新的User对象
        user = User.objects.create_user(username=username, password=password)
        
        # 创建对应的UserDetails对象并保存用户的详细信息
        user_details = UserDetails(user=user, gender=gender, birth=birth, email=email)
        user_details.save()
        
        return redirect('login')
    else:
        return render(request, 'home/register.html')

@login_required
def welcome_view(request):
    user = request.user
    return render(request, 'home/welcome.html', {'user': user})

def welcome_view(request):
    users = UserDetails.objects.all()
    return render(request, 'home/welcome.html', {'users': users})

def logout_view(request):
    logout(request)
    return redirect('login')