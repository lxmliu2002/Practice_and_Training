# 讲授7新增：learn应用的urls.py
from django.urls import path
from .views import index, courses, course, add_a_b, login, search
# learn/urls.py
urlpatterns = [
        path('', index),
        path('courses', courses),
        path('course/<int:id>', course),
        path('add/<int:a>/<int:b>', add_a_b),   # 挑战2添加
        path('login', login),
        path('search', search),                 # 挑战3添加
]
