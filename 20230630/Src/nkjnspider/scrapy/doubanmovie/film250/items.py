# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# �������� scrapy ģ��
import scrapy
# �������� item ���е� Item,Field ��
from scrapy.item import Item, Field

# ��װ������
# �����ȡ�����е�����ĳһ���ֵ�����
class Film250Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    film_name = Field()
    film_score = Field()
    film_introduction = Field()
    pass
