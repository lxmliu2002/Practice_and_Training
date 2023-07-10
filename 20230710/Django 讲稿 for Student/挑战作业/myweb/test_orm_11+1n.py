# 实现映射关系一对一、一对多 涉及相关代码，需要在 python manage shell 中执行
# 部分代码没有加上注释
from learn.models import Author, AuthorDetail

# 先获取作者表中的所有三个作者，并赋值给 a1, a2, a3
a1, a2, a3 = Author.objects.all()
a1
a2
a3
ad1 = AuthorDetail(birth_date = '1520-9-15',address = '火之国木叶村可爱大道202号',profile = '暗部队长，第七班老师，六代火影，五五开绝技拥有者',author = a1)
ad1.save();
ad2 = AuthorDetail(birth_date = '1640-7-3',address = '东海可可亚西村幸福大街007号',profile = '聪明又机灵，爱好金钱和橘子，精通航海术和气象学，会武术',author_id = a2.id)
ad2.save()
ad3, result = AuthorDetail.objects.get_or_create(birth_date = '1048-5-25',address = '濮安懿王宫邸睦亲宅18号',profile = '北宋皇帝，王安石变法支持者，击败安南，元丰改制，忧郁而逝',author = a3)

a1.authordetail
ad1

ad1.author
ad1.author_id

from learn.models import Author, Course
a1 = Author.objects.first()        # 方法 1

a1 = Author.objects.get(id=1)     # 方法 2

a1 = Author.objects.get(pk=1)   # 方法 3
a1
for c in Course.objects.all()[:3]:
    a1.course_set.add(c)
a1.course_set.all()
a1.course_set.count()
a1.course_set.remove(Course.objects.get(name='Python 异步编程'))
a1.course_set.count()
a1.course_set.all()
c3 = Course.objects.get(name='Python 异步编程')
c3.id
c3.name
c3.author
a2 = Author.objects.get(pk=2)
c3.author = a2
c3.save()
a2.course_set.all()

for c in Course.objects.filter(id__in=[4, 5]):
    c.author_id = 2
    c.save()
a3 = Author.objects.get(name='宋神宗')
a3.course_set.add(Course.objects.get(id=6))