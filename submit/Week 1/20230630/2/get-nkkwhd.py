import requests
from bs4 import BeautifulSoup

import time
import random
import csv

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
    "Mozilla/5.0 (Windows NT 6.1;textmoucle WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]
# 完成随机选取 user-agnet，实现 反 反爬 操作
request_headers = {
    'user-agent': random.choice(user_agents),
    'Referer': 'https://www.baidu.com'
}

def get_per_module_page_info(module_info,url,csv_writer):
    web_data = requests.get(url=url, headers=request_headers)
    status_code = web_data.status_code
    if status_code == 200:
        html_text = web_data.text


        # 解析为 soup 文档
        soup_document = BeautifulSoup(html_text, 'lxml')

        # 定位到每行的 tr
        module_page_elements = soup_document.select('table.righttable > tr')
        module_page_elements.pop(0)
        module_page_elements.pop()

        for module_page_element in module_page_elements:
            # 定位到每行的 td
            module_page_td_element = module_page_element.select('td')
            
            activity_url = 'http://kwhd.nankai.edu.cn' + module_page_td_element[0].find(name='a').get('href')
            activity_name = module_page_td_element[0].get_text().strip()
            activity_type = module_page_td_element[1].get_text().strip()
            activity_date = module_page_td_element[2].get_text().strip()

            activity_info = {
                'activity_url': activity_url,
                'activity_name': activity_name,
                'activity_type': activity_type,
                'activity_date': activity_date
            }
            activity_info_plus = dict(module_info, **activity_info)
            
            print(activity_info_plus)

            csv_writer.writerow(activity_info_plus)
            

def get_per_module_info(url,csv_writer):
    web_data = requests.get(url=url, headers=request_headers)
    status_code = web_data.status_code
    if status_code == 200:
        html_text = web_data.text
        # 解析为 soup 文档
        soup_document = BeautifulSoup(html_text, 'lxml')

        # 定位到每个模块超链 li 标签
        module_elements = soup_document.select('ul.bankuai.clearfix > li')

        for module_element in module_elements:
            # 提取每个模块超链
            module_urls = [url + module_element.find(name='a').get('href') + '/p/'+ str(i) for i in range (1,10,1)]
            # 提取每个模块名字
            module_name = module_element.find(name='a').find(name='p').get_text().strip()
            
            for module_url in module_urls:
                module_info = {
                    'module_url' : module_url,
                    'module_name' : module_name
                }
                get_per_module_page_info(module_info,module_url,csv_writer)

            
            time.sleep(0.5)
        




# 声明主程序入口
if __name__ == '__main__':
    # 声明|创建 top250 所有的列表页的 urls list
    url = 'http://kwhd.nankai.edu.cn'
    # 遍历每一个列表页，调用方法，获取列表页中的信息
    with open('data.csv', 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=['module_url', 'module_name', 'activity_url', 'activity_name', 'activity_type', 'activity_date'])
        csv_writer.writeheader()  # 写入表头

        get_per_module_info(url, csv_writer)
        time.sleep(0.5)
    print("End....")