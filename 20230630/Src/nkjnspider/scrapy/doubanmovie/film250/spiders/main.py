# 导入 cmdline
from scrapy import cmdline

# 执行如下命令，运行 scrapy 爬虫(爬虫的名称必须和当前项目的爬虫名称一致)
# 对应命令行命令： scrapy crawl filmspider
# cmdline.execute(['scrapy', 'crawl', 'filmspider'])
# 或者：
# cmdline.execute('scrapy crawl filmspider'.split())

# 执行如下命令，运行 scrapy 爬虫，同时将数据借助 -o 参数输出到指定的 csv 文件中
# 对应命令行命令： scrapy crawl filmspider -o doubanfilm.csv
cmd_param = "filmspider -o doubanfilm.csv"
cmd_line_str = "scrapy crawl {0}".format(cmd_param)
cmdline.execute(cmd_line_str.split())
# 或者：
# cmdline.execute(['scrapy', 'crawl', 'filmspider', '-o', 'doubanfilm.csv'])