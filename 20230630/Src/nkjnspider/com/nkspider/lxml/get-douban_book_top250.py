# 导入所需模块
import requests
from lxml import etree
from bs4 import BeautifulSoup

import time
import re
import random

# 随机给出请求头中的 user-agent
# 模拟多个 user-agent，随机选取 list 中的一个
user_agents = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]
# 完成随机选取 user-agnet，实现 反 反爬 操作
request_headers = {
    'user-agent': random.choice(user_agents),
    'Referer': 'https://www.douban.com'
}
# request_headers = {
#     'user-agent':
#         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58",
#     'Connection':
#         "keep-alive",
#     'Referer':
#         "https://www.douban.com"
# }

def get_per_page_25_book_links(url):
    web_data = requests.get(url=url, headers=request_headers)
    status_code = web_data.status_code
    if status_code == 200:
        html_text = web_data.text
        # 解析为 soup 文档
        soup_document = BeautifulSoup(html_text, 'html.parser')
        # 定位到所有图书(25本)的超链的 a 标签
        book_homepage_a_elements = soup_document.select('div.pl2 > a')
        # 遍历每一本图书
        for book_homepage_a_element in book_homepage_a_elements:
            # 提取href属性值
            book_homepage_href = book_homepage_a_element.get('href').strip()
            # 调用方法，获取每一本图书详情页面中的信息
            get_book_info(book_homepage_href)
            time.sleep(1)

def get_book_info(book_homepage_href):
    web_data = requests.get(url=book_homepage_href, headers=request_headers)
    status_code = web_data.status_code
    if status_code == 200:
        html_text = web_data.text
        # 使用 lxml 解析为 XPath 可定位的树状文档
        selector = etree.HTML(html_text)
        # 获取图书的名称
        book_name = selector.xpath('//*[@id="wrapper"]/h1/span/text()')[0].strip()
        # 获取作者信息
        # 如果图书没有作者，需要先判断元素是否存在，如果不存在，输出没有作者
        # author_name_element = selector.xpath('//*[@id="info"]/span[1]/a/text()');
        # author_name = author_name_element[0].strip() if author_name_element != 0 else "没作者";
        author_name = selector.xpath('//span[contains(text(), "作者")]')[0].tail
        # ?start=200 中的水浒传 的 作者格式还需要分析
        # 使用正则表达式，去除多余的空格
        # 1. 指定匹配规则：匹配所有的空白符
        p = re.compile('\s+')
        # 2. 删除==替换为 ''
        author_name = re.sub(p, '', author_name)
        # 获取出版社信息
        publisher_name = selector.xpath('//span[contains(text(), "出版社")]')[0].tail
        # 获取出版年信息
        publisher_date = selector.xpath('//span[contains(text(), "出版年")]')[0].tail
        # 获取定价信息
        book_price_element = selector.xpath('//span[contains(text(), "定价")]')
        book_price = book_price_element[0].tail if book_price_element!=0 else 0.0
        # 获取图书评分
        book_rate = selector.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()')[0].strip()
        # 获取 isbn 或者 统一书号
        book_isbn = selector.xpath('//span[contains(text(), "ISBN") or contains(text(), "统一书号")]')[0].tail
        print(book_name, author_name, publisher_name, publisher_date, book_price, book_rate, book_isbn)



# 声明主程序入口
if __name__ == '__main__':
    # 声明|创建 top250 所有的列表页的 urls list
    urls = ['https://book.douban.com/top250?start={}'.format(str(no)) for no in range(100, 250, 25)]
    # 遍历每一个列表页，调用方法，获取列表页中的信息
    for url in urls:
        get_per_page_25_book_links(url)
        time.sleep(0.5)
    print("End....")