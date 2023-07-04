# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import csv
class Film250Pipeline:
    def __init__(self):
        csv_fp = open('film250.csv', 'w', encoding='gb18030', newline='')
        csv_writer = csv.writer(csv_fp)
        csv_writer.writerow(('filmname', 'score', 'introduction'))
        self.post = csv_writer

    def process_item(self, item, spider):
        csv_writer = self.post
        csv_writer.writerow((item['filmname'], item['score'], item['introduction']))
        return item
