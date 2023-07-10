from django.db import models

# Create your models here.
'''
课程表映射类，包括课程名字、发布时间和学习人数等属性
'''
class Course(models.Model):
    # 定义类内属性
    # name 属性
    # 对应到数据表中的字段类型为字符串型，并设置字段最大长度。
    name = models.CharField(max_length=64)
    # pub_date 属性
    # 对应到数据表中的字段类型为 Date 日期类型
    pub_date = models.DateField()
    # stu_number 属性
    # 对应到数据表中的字段类型为 Integer 类型，并设置字段的默认值为 0
    stu_number = models.IntegerField(default=0)
    # 实现作者和课程一对多关系的新增代码
    # 只在 课程表映射类中增加，Course类设置外键主动关联Author，Author类中不需要任何修改
    author = models.ForeignKey('Author', on_delete=models.CASCADE,  # 这两行
                               null=True)  # 是新增代码

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Course: {self.name}>'

'''
挑战作业1：创建课程作者数据表:
在完成下述映射类代码后，
激活虚拟环境，在项目主目录 myweb 下，执行：
生成数据表
  python manage.py makemigrations
  python manage.py migrate
插入数据：
    执行 python manage.py shell 打开 Python Shell ：
    from learn.models import Author
    Author.objects.get_or_create(name='卡卡西', gender=1)
    Author.objects.get_or_create(name='娜美', gender=0)
    Author.objects.get_or_create(name='宋神宗')
'''
class Author(models.Model):
    '''
    课程作者映射类，包括作者名字、性别等属性
    '''

    # name = models.CharField(max_length=64)
    # 自定义管理端显示的字段名称，使用 verbose_name 参数
    name = models.CharField(max_length=64, verbose_name='姓名')
    # gender = models.BooleanField(null=True)
    # 自定义管理端显示的字段名称，在第一个位置上声明名称
    gender = models.BooleanField('性别', null=True)

    def __str__(self):
        return self.name

'''
    作者详情类，包括出生日期、地址、简介等属性
'''
class AuthorDetail(models.Model):

    birth_date = models.DateField(null=True)
    address = models.CharField(max_length=64)
    profile = models.TextField()
    author = models.OneToOneField('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.author.name

'''
课程的标签表，包括 name 属性，与 Course 为多对多关系
'''
class Tag(models.Model):

    name = models.CharField(max_length=32)
    course = models.ManyToManyField('Course')

    def __str__(self):
        return self.name
