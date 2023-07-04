# Scrapy settings for film250 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'film250'
SPIDER_MODULES = ['film250.spiders']
NEWSPIDER_MODULE = 'film250.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'film250 (+http://www.yourdomain.com)'
# 可以在此处指定user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True
# 指定不遵守 robots.txt 文件中的规则
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# 设置每次访问之间延时2秒，但不能动态改变，由于时间间隔固定，容易被发现，导致ip被封
DOWNLOAD_DELAY = 2
# 建议还是在代码中设置延迟 ==time.sleep 或者叠加使用以下配置
# 启用后，当从相同的网站获取数据时，Scrapy将会等待一个随机的值，延迟时间为0.5到1.5之间的一个随机值乘以DOWNLOAD_DELAY
RANDOMIZE_DOWNLOAD_DELAY = True
# The download delay setting will honor only one of:
# 对单个网站进行并发请求的最大值，默认为8
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
# 对单个IP进行并发请求的最大值，如果非0,则忽略CONCURRENT_REQUESTS_PER_DOMAIN设定，使用该IP限制设定。
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 启用 cookies，可以不用设置，因为默认是启用的
# COOKIES_ENABLED = False
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 此处可以设置 请求头参数
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }
# 设置请求头
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cookie': 'douban-fav-remind=1; gr_user_id=c1889e31-ba3c-4cd8-a33c-cd8c1d0a9759; Hm_lpvt_19fc7b106453f97b6a84d64302f21a04=1654860713; ucf_uid=2a534f68-80dc-470a-8759-e5eac3b76675; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1665820504; Hm_lpvt_16a14f3002af32bf3a75dfe352478639=1665820504; _ga=GA1.1.62673610.1666426103; _ga_RXNMP372GL=GS1.1.1666426103.1.0.1666426108.55.0.0; ll="108289"; bid=JEdt3gC9VRY; __yadk_uid=sV31V7SlI4f5txy1XaCmVf9QZzFezKAE; _pk_id.100001.4cf6=1b2587345817fef5.1688010127.; ct=y; viewed="1008357_1212893_33658616_2035179_1209899_3162991_1449352_33435472_1007305_2080599"; dbcl2="48860155:NZp7mlyQYnw"; ck=bSYg; push_noty_num=0; push_doumail_num=0; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1688160626%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.4cf6=1',
    'Referer': 'https://www.douban.com',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'film250.middlewares.Film250SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# 如果使用了通过中间件设置并使用代理的方式，需要打开/取消下面的注释
#DOWNLOADER_MIDDLEWARES = {
#    'film250.middlewares.Film250DownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'film250.pipelines.Film250Pipeline': 300,
#}
# 通过项目名称.管道组件文件的名称.项目管道类名 : 表示执行顺序优先级的数字(0->1000)
ITEM_PIPELINES = {
    'film250.pipelines.Film250Pipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# 自动限速扩展
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#默认为False，设置为True可以启用该扩展
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
# 初始下载延迟，单位为秒，默认为5.0
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# 设置在高延迟情况下的下载延迟，单位为秒，默认为60
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# 用于启动Debug模式，默认为False
#AUTOTHROTTLE_DEBUG = False
AUTOTHROTTLE_DEBUG = True

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
