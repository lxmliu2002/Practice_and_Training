# 导入 Scrapy 命令行工具
from scrapy import cmdline
cmd_param = "filmspider"
# cmd_param = "filmspider -o doubanfilm.csv"
cmd_line_str = "scrapy crawl {0}".format(cmd_param)