from django.db import models

# Create your models here.

class Course(models.Model):
    '''课程表映射类，包括课程名字、发布时间和学习人数等属性
    '''

    name = models.CharField(max_length=64)
    pub_date = models.DateField()
    stu_number = models.IntegerField(default=0)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Course: {self.name}>'

class Author(models.Model):
    '''课程作者映射类，包括作者名字、性别等属性
    '''

    name = models.CharField(max_length=64, verbose_name='名字')
    gender = models.BooleanField('性别', null=True)

    def __str__(self):
        return self.name


class AuthorDetail(models.Model):
    '''作者详情类，包括出生日期、地址、简介等属性
    '''

    birth_date = models.DateField(null=True)
    address = models.CharField(max_length=64)
    profile = models.TextField()
    author = models.OneToOneField('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.author.name

class Tag(models.Model):
    '''课程的标签表，包括 name 属性，与 Course 为多对多关系
    '''

    name = models.CharField(max_length=32)
    course = models.ManyToManyField('Course')

    def __str__(self):
        return self.name


