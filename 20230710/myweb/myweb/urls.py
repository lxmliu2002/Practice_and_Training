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
from django.contrib import admin
from django.urls import path, include
from front import views
# from learn.views import index, courses, course

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index),            
    # path('courses/1', courses),
    # path('course/<int:id>', course),
    path('learn/', include('learn.urls')),
    path('', views.home),
]
handler404 = views.page_not_found
handler500 = views.server_error