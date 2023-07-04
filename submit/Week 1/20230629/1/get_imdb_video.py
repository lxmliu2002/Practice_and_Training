# 导入 所需的 模块
import urllib.request
import os
'''
    0. 生成请求的 uri
'''

# 0. 生成imdb的uri
uri = 'https://imdb-video.media-imdb.com/vi3837511449/1434659607842-pgv4ql-1687556762812.mp4?Expires=1688266981&Signature=jAWqwairIE3WMfRoK3BxLJXFWhwLRpNYl~Oejb4FsvuwOZ0vRT29GX3OVxhwB-FfssHHTvM1DpWVeQJlTtkDiSj2VIHztNltLf2GpPUZjGly30KOO3VBGZBvLN~ESBox36UVLwN1BMUKSxtMVIrFA0YgQpjB3NKq36hksGHbTRmooVIeuCO27IWNFqlHD75ez4VNQHdbEw5c2MvB5nh3u1uOfj80ISZMy71T3EJiR-1qHG1IZGbO0U0GiTzwcQEgxxbCwenspOs8CvlcixyJ827EWkC1q2U1HArA64-QeHy8NCN7yQRQjC~gIDVBRAaCvWg0B8vwW0bRmlAgTU9Gxw__&Key-Pair-Id=APKAIFLZBVQZ24NQH3KA'

# 1. 指定 请求头中的 useragent
request_headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58",
    "Connection": "keep-alive",
    "Referer": "https://www.imdb.com/"
}

# 2. 封装请求， 指定请求头参数
request = urllib.request.Request(url=uri, headers=request_headers, method="GET")

# 3. 发送请求，获取响应
response = urllib.request.urlopen(request)

# 4. 获取状态码
status_code = response.getcode()

block_size = 4096  # 分块大小为4KB

# 5. 获取响应的内容
response_data = response.read()

# 执行图片的本地保存 =Python IO
file_name = "imdb.mp4"
file_path = os.path.join(os.getcwd(), 'data')
if not os.path.exists(file_path):
    os.mkdir(file_path)
# 完成写入
with open(file_path + os.sep + file_name, 'wb') as fp:
    while True:
            response_data = response.read(block_size)
            if not response_data:
                break
            fp.write(response_data)

print("End...")