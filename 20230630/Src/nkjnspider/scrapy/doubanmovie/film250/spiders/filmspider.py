# 导入所需 scrapy 模块
import scrapy
# 导入要放置数据项的 items 中的类
from film250.items import Film250Item

class FilmspiderSpider(scrapy.Spider):
    # 必写属性1： 爬虫名称
    name = 'filmspider'
    allowed_domains = ['douban.com']
    # 必写属性2：待爬取的url list，
    # 可在在后去爬取过程中，获取后续待爬取的url，发送请求（关键方法）
    # 也可以在此处，一次性的将待爬取的所有的url一次性的生成
    start_urls = [
        'https://movie.douban.com/top250?start={}'.format(str(i)) for i in range(0, 250, 25)
    ]
    # start_urls = [
    #     'https://movie.douban.com/top250?start=0'
    # ]
    '''
    # 属性3，可选，给出 request_headers == user-agent
    # 可以在本处完成说明、settings.py中、downloadermiddleware 中
    headers = {
        'User-Agent' :
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'
    }
    '''

    # 必写两方法（方法中要实现两个功能，按需书写），覆盖重写。
    # 不需要完成后续url的获取和发送请求，只需要完成抓取的数据的放入 item 中
    def parse(self, response):
        # 新建 Item 实例对象
        doubanmovie_item = Film250Item()
        # 开始爬取
        # 1- 使用 css selector 进行解析
        css_selector = response.css
        # 第一个功能：抓取页面中数据，并封装到数据项中
        # 2- 遍历每一个包含电影信息的 div
        for item in css_selector('div.item'):
            # 获取所需爬取的数据
            film_name = item.css('div.info > div.hd > a > span.title::text').extract_first();
            film_score = item.css('div.info div.bd div.star span.rating_num::text').extract();
            film_instroduction = item.css('div.info div.bd p.quote span.inq::text').extract();
            # 将爬取数据的组成部分，某些数据项放入 item 中
            doubanmovie_item['film_name'] = film_name
            doubanmovie_item['film_score'] = film_score
            doubanmovie_item['film_introduction'] = film_instroduction
            # 将 item 交给 scrapy 框架处理 -- 借助异步方式
            yield doubanmovie_item
        # 第二个功能：抓取页面中待爬取的后续其他url，并提交到 scrapy 的请求列表中，由 scrapy 的 scheduler 处理
        # scrapy scheduler 有 url 去重功能
        # 注意：如果在前面的 start_urls 列表中具有全部待爬取的 url，此功能可以不写
        # 3- 获取页面中后续url，并提交到 scrapy 的 request 列表中
        # 获取页面的 '后页' 超链元素的值
        next_url = response.css('div.paginator > span.next > a::attr(href)').extract()
        # 判断 '后页' 是否为空（最后一页时，'后页'链接值为空）
        if next_url:
            # 页面中 后页 的值为：?start=xx&filter= 的形式
            # 需要去除 &filter= 的部分，然后拼接为真是的下一页的url
            # 去除 &filter= 的部分，目的是为了保证和 start_urls 中的链接值一致，才可以实现 scrapy scheduler 去重
            # 获取 后页 链接中的 & 字符的位置
            and_pos = next_url[0].index('&')
            # 使用切片功能，获取 ?start=xx 的值
            next_url_in_page = next_url[0][0:and_pos]
            print(next_url_in_page)
            # 拼接生成真实的后页 url
            real_next_url = "http://movie.douban.com/top250" + next_url_in_page
            print(real_next_url)
            # 将获取的真实后页url异步提交到request请求的url列表中
            # 如果当前程序设置了headers，就提供headers参数
            # yield scrapy.Request(url=real_next_url, headers=self.headers)
            yield scrapy.Request(url=real_next_url)
            # 设置使用代理，也可以在 middlewares.py 中设置
            '''
            在 此处设置并使用 代理
            proxy = "http://180.175.2.68:8060"
            yield scrapy.Request(url=real_next_url, meta={"proxy": proxy})
            '''
        pass

    # 方法：可选方法
    # 如果 start_urls 中含有待爬取的所有的url列表，此方法可以不写
    # 即使写了，可以借助 scrapy scheduler 的去重功能完成 url 去重
    def start_requests(self):
        # 遍历所有待爬取的 urls list ==start_urls，逐个发出请求
        # scrapy 有url去重功能
        for url in self.start_urls:
            # 给出3个参数 url\headres\处理获取响应的回调函数名称
            # yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)
            # 如果当前类中没有设置 请求头参数，则不同提供headers参数
            yield scrapy.Request(url=url, callback=self.parse)
            # 设置使用代理，也可以在 middlewares.py 中设置
            '''
            在 此处设置并使用 代理
            proxy = "http://180.175.2.68:8060"
            yield scrapy.Request(url=url, meta={"proxy": proxy})
            '''
        pass
