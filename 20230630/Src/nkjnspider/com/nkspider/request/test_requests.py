# 导入所需模块
import requests

# 生成 url
url = "https://movie.douban.com/review/best/"

request_headers = {
    'user-agent':
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58",
    'Connection':
        "keep-alive",
    'Referer':
        "https://www.douban.com"
}

# 发送请求获取响应
resp = requests.get(url=url, headers=request_headers)

# 获取并处理响应
status_code = resp.status_code
if status_code == 200:
    html_text = resp.text
    print(html_text)