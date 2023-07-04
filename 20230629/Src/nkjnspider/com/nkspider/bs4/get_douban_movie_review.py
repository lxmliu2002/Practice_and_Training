# 导入所需的 模块
import requests
from bs4 import BeautifulSoup
import lxml

# 1. 生成 url
url_str = 'https://movie.douban.com/review/best/?start=0'
# url_strs = 'https://movie.douban.com/review/best/?start={}'.format(str(i) for i in range(0, 100, 10))



# 2. 封装请求，并发送、获取响应文本
request_headers = {
    'user-agent':
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58",
    'Connection':
        "keep-alive",
    'Referer':
        "https://www.douban.com"
}
resp = requests.get(url=url_str, headers=request_headers)
status_code = resp.status_code
if status_code == 200:
    html_text = resp.text

# 3. 使用 BeautifulSoup4 解析 htmlText
soup = BeautifulSoup(html_text, 'lxml')     # html.parser/lxml/xml

# 4. 使用 css selector 完成定位
# author_names = soup.find(name='a', class_='name')
# author_href = soup.find(name='a', href='http://www.douban.com/people/111...')
# 定位所有的作者信息
author_info_elements = soup.select("a.name")
# 定位所有的电影信息
movie_info_elements = soup.select("a.subject-img")

# 便利所有的信息
for author_info_element, movie_info_element in zip(author_info_elements, movie_info_elements):
    # 获取作者的名字, 标签体内容值
    author_name = author_info_element.get_text().strip()
    # 获取作者的主页，标签属性 href 的值
    author_homepage = author_info_element.get("href").strip()
    # 获取电影信息，首先获取 其下的 img 标签
    movie_info_img_element = movie_info_element.find(name='img')
    # 获取电影名字
    move_name = movie_info_img_element.get('title')
    move_homepage = movie_info_element.get('href')
    move_cover_img_url = movie_info_img_element.get('src')

    # 封装字典中
    movie_review_info = {
        'author_info_name' : author_name,
        "author_homepage" : author_homepage,
        "move_name" : move_name,
        "move_homepage" : move_homepage,
        "move_cover_img_url" : move_cover_img_url
    }

    print(movie_review_info)