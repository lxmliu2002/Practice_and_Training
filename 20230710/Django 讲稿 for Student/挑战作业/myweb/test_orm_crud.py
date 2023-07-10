# 映射类的增删改查操作 涉及相关代码，需要在 python manage shell 中执行
# 引入映射类
from learn.models import Course

# 查询 learn_course 数据表中的全部数据
all_courses = Course.objects.all()
all_courses

# 变量 all_courses 是 QuerySet 类的对象，是 “查询集”
# 该对象为可迭代对象，使用 isinstance 函数可以判断
from collections import Iterable
isinstance(all_courses, Iterable)
#上面的方法已经降级，建议改为：
from collections.abc import Iterable
isinstance(all_courses, Iterable)

# 可迭代对象，使用 for 关键字对其进行迭代获取元素
for course in all_courses:
    # 在创建映射类的时候，定义了 __str__ 方法
    print(course)
for course in all_courses:
    # course 是 Course 类的实例，可以打印它的其它属性
    print('Name: {}, Pub_date: {}, Stu_number: {}'.format(course.name, course.pub_date, course.stu_number))

# 使用 Course.objects 的 filter 方法过滤数据
for course in Course.objects.filter(stu_number__gt=99):
    print('课程名字：{}, 发布日期：{}'.format(course.name, course.pub_date))

# 使用 exclude 方法过滤掉（去除）符合条件的数据
for course in Course.objects.exclude(stu_number__gt=99):
    print('课程名字：{}, 发布日期：{}'.format(course.name, course.pub_date))

# get 方法只返回一个符合的映射类实例（不支持条件运算符，可以提供多个参数）
# 查找 id 字段值为 2 的课程
c = Course.objects.get(id=2)
c
c.name
# 查找 id 字段值为 2 且 name 字段值为 "Git 与 Github 入门实践" 的课程
c = Course.objects.get(id=2, name='Git 与 Github 入门实践')
c
c.id
c.name

for course in Course.objects.filter(stu_number__gt=99):
    print('课程名字：{}, 发布日期：{}'.format(course.name, course.pub_date))
# order_by 对 QuerySet 对象进行排序，也就是对查询结果进行排序，参数就是字段名的字符串。
for course in Course.objects.filter(stu_number__gt=99).order_by('pub_date'):
    print('课程名字：{}, 发布日期：{}'.format(course.name, course.pub_date))
# 降序排序，只需在属性字符串前面加个减号 order_by('-pub_date')
for course in Course.objects.filter(stu_number__gt=99).order_by('-pub_date'):
    print('课程名字：{}, 发布日期：{}'.format(course.name, course.pub_date))

from datetime import datetime
# 按学生数量倒序排序，打印课程 id 、pub_date 和 stu_number
for course in Course.objects.filter(pub_date__lt=datetime(2000, 1, 1).date()).order_by('-stu_number'):
    print('ID: {}, Date: {}, Stu: {}'.format(course.id, course.pub_date, course.stu_number))
# pub_date__lt 的值没必要构造 Date 类型的数据，直接使用字符串亦可
# 因为 MySQL 服务器自己会进行数据类型转换
for course in Course.objects.filter(pub_date__lt='2000-1-1').order_by('-stu_number'):
    print('ID: {}, Date: {}, Stu: {}'.format(course.id, course.pub_date, course.stu_number))
    print(course.name)
# 打印学生数量为 728 的课程的名字，注意，stu_number是由faker生成，具体数值需要视情况而定
for course in Course.objects.filter(stu_number__exact=728):
    print(course.name)
for course in Course.objects.filter(stu_number__exact=590):
    print(course.name)

# 查询并打印课程名字中带大写字母 L 的课程的 id 和 name
for course in Course.objects.filter(name__contains='L'):
    print('ID: {}, Name: {}'.format(course.id, course.name))
# 如果字母不区分大小写呢？在 contains 前面加上一个字符 i 即可
for course in Course.objects.filter(name__icontains='L'):
    print('ID: {}, Name: {}'.format(course.id, course.name))
# 查询课程名字中包含 Docker 的课程，打印课程的 id 和 name
for course in Course.objects.filter(name__icontains='docker'):
    print('ID: {}, Name: {}'.format(course.id, course.name))
# 查询课程名字以 “教程” 二字结尾的课程，打印课程的 id 和 name
for course in Course.objects.filter(name__endswith='教程'):
    print('ID: {}, Name: {}'.format(course.id, course.name))
# 查询课程名字以 “python” 开头的课程，不区分大小写，打印课程的 id 和 name
for course in Course.objects.filter(name__istartswith='python'):
    print('ID: {}, Name: {}'.format(course.id, course.name))

# 范围运算符 in ，参数为列表，用于查询字段值在列表中的数据。
# 查询 id 字段值为 1 或 3 或 7 的课程，打印课程的 id 和 name
for course in Course.objects.filter(id__in=[1, 3, 7]):
    print('ID: {}, Name: {}'.format(course.id, course.name))
# 查询任意年 1 月份发布的课程
for course in Course.objects.filter(pub_date__month=1):
    print('Date: {}, Name: {}'.format(course.pub_date, course.name))

# 聚合函数
'''
Course.objects.aggregate 方法的返回值是一个字典，字典中只有一组键值对。
其中 key 是使用双下划线把字段名和类名的全小写连起来生成的字符串，value 就是计算结果。
求学生人数的总和，aggregate :
方法的返回值字典的 key 就是 stu_number__sum ，其中 stu_number 是字段名，sum 是求和类 Sum 的全小写。
'''
from django.db import models
Course.objects.aggregate(models.Sum('stu_number'))
Course.objects.aggregate(models.Avg('stu_number'))
Course.objects.aggregate(models.Max('stu_number'))
Course.objects.aggregate(models.Min('stu_number'))
Course.objects.aggregate(models.Count('stu_number'))
# Course.objects 本身就有 count 方法获取数量
Course.objects.count()

# 获取映射类实例，修改实例属性，调用实例的 save 方法
c3 = Course.objects.get(id=3)
c3.id
c3.name
c3.pub_date
# 修改属性值
c3.pub_date = '2019-4-3'
# 调用 save 方法保存修改到数据库
c3.save()

# 查询数据库获取类的实例对象，然后调用实例的 delete 方法删除自身
c7 = Course.objects.get(id=7)
c7.id
c7.name
# 删除 id 为 7 的课程
c7.delete()