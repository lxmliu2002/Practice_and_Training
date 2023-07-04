# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# 导入所需 scrapy 模块
import scrapy
# 导入所需 item 包中的 Item,Field 类
from scrapy.item import Item, Field

# 封装数据项
# 完成爬取数据中的数据某一部分的命名
class Film250Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    film_name = Field()
    film_score = Field()
    film_introduction = Field()
    pass
