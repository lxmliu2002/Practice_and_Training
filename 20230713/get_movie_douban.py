import time
import random

from requests_html import HTMLSession, UserAgent

url = "https://movie.douban.com/"

# 0. 创建连接 -html连接
seesion = HTMLSession()

# 1. User-Agent 选择
# 借助 requests-html UserAgent 类型
# user_agent = UserAgent().random
# 使用自有的 User-Agent
# user_agent = Edge-User-Agent
# 自行生成 User-Agent 可用列表，自行随机选取
search_engine_UA_list=[
    # 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
    # 'Mozilla/5.0 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)',
    #'Mozilla/5.0 (Windows NT 6.1; Win64; x64)',
    # ok
    'AppleWebKit/537.36 (KHTML, like Gecko)',
    #'Chrome/69.0.3497.81 YisouSpider/5.0 Safari/537.36',
    # 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    #'Sogou+web+spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)',
    # ?'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    # 'Sosospider+(+http://help.soso.com/webspider.htm)',
    #'Mozilla/5.0 (compatible; Yahoo! Slurp China; http://misc.yahoo.com.cn/help.html)',
    # 'Mozilla/5.0 (compatible; Bytespider; https://zhanzhang.toutiao.com/) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.0.0 Safari/537.3'
]
user_agent = random.choice(search_engine_UA_list)
request_headers = {"User-Agent": user_agent}

# 2. 发送请求，获取响应
resp = seesion.get(url=url, headers=request_headers, timeout=(2, 5), verify=False)
time.sleep(2)

status_code = resp.status_code
if  status_code == 200:
    # 3. 进行动态渲染
    resp.html.render(sleep=2, retries=3)
    # 获取响应的动态刷新之后 html 文本
    html_text = resp.html.html
    print(html_text)
    # 4. 解析、定位、提取
    # 讲 获取的动态数据的 html_text 放入 BeautifulSoup4 种， 解析、定位、提取
    # 5. 借助 requests-html 自身的解析、定位、提取
    # cssselector
    elements_cssselector = resp.html.find("div.slide-page a")
    # xpath
    elements_xpath = resp.html.xpath('.//div[@class="slide-page"]/a')
    movie_elements =resp.html.find("div.gaia.gaia-lite.gaia-movie.slide-mode a.item")

    for movie_element in movie_elements:
        title = movie_element.find('p')[0].text
        rate = movie_element.find('p strong')[0].text
        homepage_url = movie_element.attrs.get('href')
        img_url = movie_element.find('img')[0].attrs.get('src')
        print(title, rate, homepage_url, img_url)
    print(len(elements_cssselector))
    print(len(elements_xpath))
    print(len(movie_elements))

# 最后关闭连接
seesion.close()

