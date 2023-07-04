import urllib.request
import urllib.parse

url = "https://book.douban.com"
request_headers = {
    'user-agent':
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58",
    'Connection':
        "keep-alive",
    'Referer':
        "https://www.douban.com"
}
request = urllib.request.Request(url=url, headers=request_headers, method="GET")
response = urllib.request.urlopen(request)
status_code = response.getcode()
response_info = response.info()
response_headers = response.getheaders()
content_type = response.getheader("Content-Type")
request_address = response.geturl()
html_text = response.read().decode('utf-8')
print(html_text)


print('=============================')
'''
带着请求参数，发送请求
'''
url_baidu_request = "https://www.baidu.com/s"
request_params = {'wd': '天津'}
request_data = urllib.parse.urlencode(request_params)
baidu_query_real_url = url_baidu_request + '?' + request_data
baidu_query_request = urllib.request.Request(url=baidu_query_real_url,
                                 headers=request_headers,
                                 method="GET")
baidu_query_response = urllib.request.urlopen(baidu_query_request)
status_code = baidu_query_response.getcode()
if status_code == 200:
    print(baidu_query_response.read().decode('utf-8'))
