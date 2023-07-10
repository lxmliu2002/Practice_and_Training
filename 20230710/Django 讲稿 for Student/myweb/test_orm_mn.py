# 实现映射关系多对多 涉及相关代码，需要在 python manage shell 中执行
# 多对多的数据表的创建方式，以及数据的增删查操作
from learn.models import Tag, Course
t1 = Tag.objects.get(pk=1)
t1
t1.name
c3, c5 = Course.objects.filter(id__in=[3, 5])
c3.name
c5.name
t1.course.add(c3)
t1.course.add(c5)
t1.course.all()
c3.tag_set.add(Tag.objects.get(name='Linux'))
c3.tag_set.add(Tag.objects.get(name='Git'))
c3.tag_set.all()
c3.tag_set.remove(t1)
c3.tag_set.all()
t1.course.all()
t1.course.remove(c5)
t1.course.all()

# 多表查询 涉及相关代码，需要在 python manage shell 中执行
# 一对一关系，查询卡卡西的作者详情实例
from learn.models import Author, AuthorDetail
result = AuthorDetail.objects.filter(author__name='卡卡西')
result
result[0]

# 一对多关系，查询娜美的全部课程的列表
result = list(Course.objects.filter(author__name='娜美'))
result

# 查询课程名字中包含 ”教程“ 二字的作者的实例列表
result = list(Author.objects.filter(course__name__contains='教程'))
result

# 多对多关系，查询 id 为 3 的课程有哪些标签
result = list(Tag.objects.filter(course__id=3))
result

# 添加多对多关系
t2 = Tag.objects.get(id=2)
t8 = Tag.objects.get(id=8)
t2.course.add(Course.objects.get(id=1))
t8.course.add(Course.objects.get(id=2))
# 查询 Linux 或 Git 标签的全部课程列表
result = list(Course.objects.filter(tag__name__in=['Linux', 'Git']))
result
# 重重（先set再list）
result = list(set(Course.objects.filter(tag__name__in=['Linux', 'Git'])))
result

