# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# 导入所需模块
from itemadapter import ItemAdapter
# 导入 csv 模块
import csv


class Film250Pipeline:
    # 在当前类被调用的时候，最初执行并仅执行一次，进行初始化
    def __init__(self):
        # 打开指定文件
        csv_fp = open('film250.csv', 'w', encoding='gb18030', newline='')
        # 获取 csv 文件的写指针
        csv_writer = csv.writer(csv_fp)
        # 向 csv 文件中写入一行表头
        # csv 文件中的一行，是要给 tuple 类型，要用 () 括起来
        csv_writer.writerow(('name', 'score', 'introduction'))
        # 暂存 csv 文件的写指针
        self.post = csv_writer

    # 处理传过来的一个item(doubanmovieitem)，
    def process_item(self, item, spider):
        # 获取暂存的 csv 文件的写指针
        csv_writer = self.post
        # 逐一向 csv 文件中写入每一个数据项
        csv_writer.writerow((item['film_name'], item['film_score'], item['film_introduction']))
        return item
