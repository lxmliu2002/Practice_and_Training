# 导入所需的模块，内置 urllib
import urllib.request

'''
    0. 准备要访问的 uri(url)
        https://www.baidu.com
    1. 发送请求
    2. 获取响应 
    3. 处理响应
'''

# 0. 生成 uri ==url
url = "http://www.baidu.com"

# 1. 封装请求（提供了要访问的url，访问的方法）
request = urllib.request.Request(url=url, method="GET")

# 2. 发送请求，并获取响应
response = urllib.request.urlopen(request, timeout=5)

# 3. 处理响应
# 3-1 获取响应的状态码
status_code = response.status
print("status_code:", status_code)
# 3-2 获取响应的 html text
html_txt = response.read().decode('utf-8')
print("HtmlText:", html_txt)
# 3-3 获取响应头信息
response_headers = response.getheaders()
print("Response Headers:", response_headers)
content_type = response.getheader("Content-Type")
print("ContentType:", content_type)
