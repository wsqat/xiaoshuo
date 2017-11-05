# -*- coding: utf-8 -*-

from scrapy import cmdline
import time  
from threading import Timer  
from datetime import datetime, timedelta  
from time import sleep  
  
SECONDS_PER_DAY = 24 * 60 * 60  
  
def run_crawlall( enter_time ):  
    cmdline.execute("scrapy crawlall".split())
    print "now is "+str(datetime.now()) + "run_crawlall time is " + str(enter_time)

# 规定某个时候执行此函数
def doFirst():  
    curTime = datetime.now()
    print curTime
    # 当前执行时间
    desTime = curTime.replace(year=2017,month=11,day=3,hour=12, minute=38, second=30, microsecond=0)  
    print desTime  
    delta = desTime-curTime  
    sleeptime = delta.total_seconds()  
    print "Now day must sleep "+str(sleeptime)+ " seconds"
    sleep(sleeptime)  
    run_crawlall(datetime.now())  

if __name__ == "__main__":  
    doFirst()
# cmdline.execute("scrapy list".split())
# cmdline.execute("scrapy crawl xxsy".split())
# cmdline.execute("scrapy crawl qidian".split())
# cmdline.execute("scrapy crawl seventeen".split())
# cmdline.execute("scrapy crawl qidianmm".split())
# cmdline.execute("scrapy crawl zongheng".split())
# cmdline.execute("scrapy crawl chuangshi".split())
# cmdline.execute("scrapy crawl qidian".split())
# cmdline.execute("scrapy crawl dingdian -o dingdian.csv".split())
# from scrapy.cmdline import execute
# execute(['scrapy', 'crawl', 'dingdian'])
# 保存爬取到的数据
# cmdline.execute("scrapy crawl douban -o films.json".split())
# 保存成CSV,然后用EXCEL打开即可
# cmdline.execute("scrapy crawl douban -o items.csv -t csv".split())