# 导入所需的 模块
import requests
from bs4 import BeautifulSoup
import lxml
import time



# 1. 生成 url


url_strs = ['https://movie.douban.com/review/best/?start={}'.format(str(i)) for i in range(0, 100, 10)]



# 2. 封装请求，并发送、获取响应文本
request_headers = {
    'user-agent':
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67",
    'Connection':
        "keep-alive",
    'Referer':
        "https://www.douban.com"
}
for url_str in url_strs:
    resp = requests.get(url=url_str, headers=request_headers)
    status_code = resp.status_code
    if status_code == 200:
        html_text = resp.text

    # 3. 使用 BeautifulSoup4 解析 htmlText
    soup = BeautifulSoup(html_text, 'lxml')     # html.parser/lxml/xml

    # 4. 获取所有信息的div
    review_divs = soup.select("div.main.review-item")

    for review_div in review_divs:
        # 提取电影信息，先获取其下的 a 标签，再获取其下的 img 标签
        movie_info_element = review_div.find(name='a')
        movie_info_img_element = movie_info_element.find(name='img')

        movie_name = movie_info_img_element.get('title')
        movie_homepage = movie_info_element.get('href')
        movie_cover_img_url = movie_info_img_element.get('src')

        # 提取作者信息，先获取其下的 header 标签
        movie_author_element = review_div.find(name='header')

        movie_author_name = movie_author_element.find(name='a',class_='name').get_text().strip()
        movie_author_homepage = movie_author_element.find(name='a').get('href').strip()
        if movie_author_element.find(name='span').get('title'):
            movie_author_rate = movie_author_element.find(name='span').get('title').strip()
        else:
            movie_author_rate = "none"
        movie_author_date = movie_author_element.find(name='span',class_='main-meta').get_text().strip()
        
        # 提取影评信息,先获取其下的 div 标签
        review_info_element = review_div.find(name='div')

        review_title = review_info_element.find(name='h2').find(name='a').get_text().strip()
        review_content = review_info_element.find(name='div').find(name='div').get_text().strip()

        # 封装信息
        movie_review_info = {
            'author_info_name' : movie_author_name,
            "author_homepage" : movie_author_homepage,
            "author_rate" : movie_author_rate,
            "author_date" : movie_author_date,
            "movie_name" : movie_name,
            "movie_homepage" : movie_homepage,
            "movie_cover_img_url" : movie_cover_img_url,
            "review_title" : review_title,
            "review_content" : review_content
        }
        print(movie_review_info)
    time.sleep(1)

