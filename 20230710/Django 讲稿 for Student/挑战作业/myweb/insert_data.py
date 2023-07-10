import django; django.setup()
from datetime import datetime
from faker import Faker
import random

from learn.models import Course


fake = Faker('zh-cn')
name_list = ['Django 入门与实践', 'C++ 实现简易 Docker 容器', 'Flask 实现问答社区']


def create_courses():
    for name in name_list:
        course = Course(name=name, pub_date=fake.date(), stu_number=random.randint(100, 1000))
        course.save()


if __name__ == '__main__':
    '''在代码中操作环境变量：
    # 配置临时环境变量，只在代码运行时生效
    import os
 
    # 设置环境变量
    os.environ['keyE']="value"
    # 获取环境变量方法1
    os.environ.get('key')
    #获取环境变量方法2(推荐使用这个方法)
    os.getenv('key')
    如：
    os.getenv('path')
    # 删除环境变量
    del os.environ['key']
     
    #设置常见环境变量
    os.environ['http_proxy']:代理url(如127.0.0.1:8888）
    os.environ['HOMEPATH']:当前用户主目录
    os.environ['TEMP']:临时目录路径
    os.environ['PATHEXT']:可执行文件
    os.environ['SYSTEMROOT']:系统主目录
    os.environ['LOGONSERVER']:机器名
    os.environ['PROMPT']:设置提示符
    
    #永久设置环境变量，通过命令行将环境变量写入配置（不推荐）
    import os
    path=r"E:\env"
    # 设置环境变量 WORK1 的值为 e:\env
    command =r"setx WORK1 %s /m"%path
    os.system(command)
    #   /m代表系统变量。
    #   不加/m为用户变量
    '''
    create_courses()
