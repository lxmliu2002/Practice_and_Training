# 导包
import scrapy
from film250.items import FilmItem

#声明爬虫类
    # 1. 继承指定的父类Spider
    # 2. 完成 2+1(可选)属性，覆盖实现2个方法
class filmspider(scrapy.Spider):
    # 1. 属性1：必写、指定爬虫名称
    name = 'filmspider'
    # 2. 属性2：必写、起始url，本质上也是保存所有待爬取的url的list
    start_urls = [
        "https: // movie.douban.com / top250"
    ]
    # 3. 属性3：可选、给出 headers 中的数据 ==user-agent
    headers = {
        'user-agent':
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58",
        'Connection':
            "keep-alive",
        'Referer':
            "https://www.douban.com"
    }

    # 覆盖重写1+1个方法
    # 方法1：可选方法
    def start_requests(self):
        # 遍历所有待爬取的 urls list ==start_urls，逐个发出请求
        for url in self.start_urls:
            # 给出3个参数 url\headres\处理获取响应的回调函数名称
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)

    # 方法2：必写方法，对响应数据进行处理
    def parse(self, response):
        # 进行解析
        css_selector_document = response.css
        film_info_elements = css_selector_document('div.item')
        for film_info_element in film_info_elements:
            # yield {
            #     "film_name": film_info_element.css('div.info > div.hd > a > span.title::text').extract_first(),
            #     "score":film_info_element.css('div.info div.bd div.star span.rating_num::text').extract_first(),
            #     "introduction":film_info_element.css('div.info div.bd p.quote span.inq::text ').extract_first()
            # }
            film_name = film_info_element.css('div.info > div.hd > a > span.title::text').extract_first()
            score = film_info_element.css('div.info div.bd div.star span.rating_num::text').extract_first()
            introduction = film_info_element.css('div.info div.bd p.quote span.inq::text ').extract_first()
            film_item = FilmItem()
            film_item['film_name'] = film_name
            film_item['score'] = score
            film_item['introduction'] = introduction
            yield film_item
        next_url =response.css('div.paginator > span.next > a::attr(href)').extract()
        print(next_url)
        if next_url:
            next_url = "http://movie.douban.com/top250" + next_url[0]
            print(next_url)
            yield scrapy.Request(url=next_url, headers=self.headers)