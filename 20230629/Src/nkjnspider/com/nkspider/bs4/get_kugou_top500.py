# 导入所需模块
import requests
from bs4 import BeautifulSoup
import lxml
import time

# 给出请求头信息

request_headers = {
    'user-agent':
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58",
    'Connection':
        "keep-alive",
    'Referer':
        "https://www.douban.com"
}

# 完成某个具体页面的数据爬取
def get_info(url):
    resp = requests.get(url=url, headers=request_headers)
    # 忽略了 状态码的判断
    html_text = resp.text
    soup_document = BeautifulSoup(html_text, 'lxml')
    ranks = soup_document.select('span.pc_temp_num')
    song_infos =soup_document.select('div.pc_temp_songlist > ul > li > a')
    times = soup_document.select("#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span")
    for rank, song_info, time in zip(ranks, song_infos, times):
        rank_no = rank.get_text().strip()
        song = song_info.get('title').split('-')[1].strip()
        singer = song_info.get('title').split('-')[0].strip()
        duration = time.get_text().strip()
        data = {
            "rank_no" : rank_no,
            "song" : song,
            "singer" : singer,
            "duration" : duration
        }
        print(data)




# 主方法
if __name__ == "__main__":
    # 生成带爬取的所有的页面 list  ==urls
    urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html'.format(str(i)) for i in range(1, 24)]
    print(urls)
    for url in urls:
        get_info(url)
        time.sleep(1)

    print('End....')
