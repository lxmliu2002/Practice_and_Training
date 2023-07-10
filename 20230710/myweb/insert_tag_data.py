# 配置临时环境变量，只在代码运行时生效
import os
# 设置环境变量，必须放在最开始
os.environ['DJANGO_SETTINGS_MODULE']="myweb.settings"
# 导入django，同时初始化 Django 环境
import django; django.setup()
from learn.models import Tag, Course

if __name__ == '__main__':
    name_list = ['Python', 'Linux', 'Web', '网络安全', 'C++', '数据库', 'Julia', 'Git']
    for name in name_list:
        Tag(name=name).save()
