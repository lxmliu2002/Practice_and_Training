"""
URL configuration for myweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
''' 没有使用路由转发功能的旧有路由描述
from django.contrib import admin
from django.urls import path
# from learn.views import index   # 引入视图函数
from learn.views import index, courses, course    # 引入 相关的 视图函数
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),                 # 新增路由映射
    path('helloworld', index),       # 新增另一个路由映射
    path('courses', courses),        # 新增路由与对应的视图函数生成新的接口，对应course视图
    # path('courses/1', courses)     # 新增路由与对应的视图函数生成新的接口，对应course视图
    path('course/<int:id>', course),    # 增加网址到视图函数的映射
]
'''

# 以下是讲授7中，带有路由转发功能的路由描述
from django.contrib import admin
from django.urls import path, include  # 引入 include 方法
from front import views # 新增代码

# myweb/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('learn/', include('learn.urls'))
]

# 指定处理
# 指定404异常处理
handler404 = views.page_not_found # 新增代码
# 指定500异常处理
handler500 = views.server_error # 新增代码

