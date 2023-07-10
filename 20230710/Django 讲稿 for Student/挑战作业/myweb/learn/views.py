from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World.')

# 讲授7中，新增视图函数代码
# 引入所需映射类
from .models import Course
""" 简单的响应
# 新建视图函数
def courses(request):
    # 从数据库中获取全部课程数据
    courses = Course.objects.all()
    s=""
    for course in courses:
        s+=str(course)
        # 使用 </br> 标签将各个课程数据连起来生成字符串
        # 其中 </br> 标签在浏览器页面上起到换行的作用
        s+="</br>"
    return HttpResponse(s)
"""
# 带有模板引擎渲染且夹带返回数据的响应
def courses(request):
    courses = Course.objects.all()
    # return render(request, 'learn/courses.html', {'courses': courses})
    return render(request, 'learn/courses.html', context={'courses': courses})


# def course(request, id):
# 指定请求方法为：GET
""" 简单的响应返回
def course(request, id, method=['GET']):
    course = Course.objects.get(id=id)
    s = 'ID: {}</br>Name: {}</br>发布时间：{}</br>学生人数：{}'.format(
            course.id, course.name, course.pub_date, course.stu_number)
    return HttpResponse(s)
"""
# 基于模板引擎且夹带返回数据的渲染返回
from datetime import datetime

def course(request, id, method=['GET']):
    course = Course.objects.get(id=id)
    date = datetime.now()
    context = {'course': course, 'date': date}
    return render(request, 'learn/course.html', context)




# 模拟登录
# def login(request):
""" 简单的模拟登录
def login(request, methods=['GET', 'POST']):
    # name = request.GET.get('name')
    name = request.POST.get('name')
    # password = request.GET.get('password')
    password = request.POST.get('password')
    if name == 'test' and password == 'test':
        return HttpResponse('登录成功')
    return render(request, 'learn/login.html')
"""
"""
# 带有 cookies 的登录功能实现
def login(request, methods=['GET', 'POST']):
    if request.method == 'GET':
        name = request.COOKIES.get('name') or 'Stranger'
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        if name == 'test' and password=='test':
            resp = HttpResponse('登录成功，{}'.format(name))
            # resp.set_cookie('name', name)
            # 设置 Cookies 的生存周期（存续时间，单位为：秒）
            # resp.set_cookie('name', name, 30, path='/learn')  # 修改这一行
            resp.set_cookie('name', name, max_age=30, path='/learn')  # 修改这一行
            return resp
    # return render(request, 'learn/login.html', {'name': name})
    return render(request, 'learn/login.html', context={'name': name})
"""
# 带有 session 功能的登录实现
def login(request, methods=['GET', 'POST']):
    if request.method == 'GET':
        name = request.COOKIES.get('name')
        sessionid = request.COOKIES.get('sessionid')
        if request.session.exists(sessionid):
            resp = HttpResponse('您已处于登录状态，{}'.format(name))
            return resp
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        if name == 'test' and password=='test':
            request.session['name'] = name
            resp = HttpResponse('登录成功，{}'.format(name))
            # resp.set_cookie('name', name, 60 * 5, path='/learn')
            resp.set_cookie('name', name, max_age=60 * 5, path='/learn')
            return resp
    # return render(request, 'learn/login.html', {'name': name})
    return render(request, 'learn/login.html', context={'name': name})


# 挑战2代码
def add_a_b(request, a, b):
    return HttpResponse(a+b)

# 挑战3代码
from learn.models import Author, Course
def search(request, methods=['GET', 'POST']):
    name = request.POST.get('name')
    try:
        author = Author.objects.get(name=name) if name else None
    except Author.DoesNotExist:
        author = None
    courses = Course.objects.filter(author=author) if author else []
    return render(request, 'learn/search.html', {'courses': courses})