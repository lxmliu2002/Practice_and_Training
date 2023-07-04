# 导入 所需的 模块
import urllib.request
import os
'''
    0. 生成请求的 uri
'''

# 0. 生成百度图片log的uri
uri = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'

# 1. 指定 请求头中的 useragent
request_headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58",
    "Connection": "keep-alive",
    "Referer": "https://www.douban.com"
}

# 2. 封装请求， 指定请求头参数
request = urllib.request.Request(url=uri, headers=request_headers, method="GET")

# 3. 发送请求，获取响应
response = urllib.request.urlopen(request)

# 4. 获取状态码
status_code = response.getcode()

# 5. 获取响应的内容
response_data = response.read()

# 执行图片的本地保存 =Python IO
file_name = "baidu.png"
file_path = os.path.join(os.getcwd(), 'data')
if not os.path.exists(file_path):
    os.mkdir(file_path)
# 完成写入
with open(file_path + os.sep + file_name, 'wb') as fp:
    fp.write(response_data)

print("End...")






