# coding:utf-8
import scrapy
import re
from scrapy.http import Request
from xiaoshuo.items import XiaoshuoItem
from scrapy.selector import Selector
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Chuangshi(scrapy.Spider):
    name = "chuangshi"
    allowed_domains = ["chuangshi.qq.com"]
    bash_url = "http://chuangshi.qq.com/bk/"
    #http://chuangshi.qq.com/bk/p/2.html
    start_urls = ['http://chuangshi.qq.com/bk/p/%s.html' % i for i in [1,500,1000]]
    bashurl = '.html'

    def start_requests(self):
        # for i in range(1,11):
        max_num = 1680 # 获取当前页面的最大页码数
        print u"当前开始爬取创世小说网……"
        for i in range(1, int(max_num)+1):
        # for i in range(1, 3):
        #     print  "当前页数："+str(max_num)
            url = self.bash_url + "p/" + str(i) + self.bashurl
            print url
            yield Request(url, dont_filter=True, callback=self.get_name)  # 将新的页面url的内容传递给get_name函数去处理

    def get_name(self, response):
        myPgae = response.body
        unicodePage = myPgae.decode('utf-8')
        # print  myPgae
        # 根据正则表达式拿到所有的内容
        novelsTable = re.findall(r'<table border="0">(.*?)</table>', unicodePage, re.S)  # 获取当前页面的Table
        # print novelsTable[0]
        novelsList = re.findall(r'<tr>(.*?)</tr>', unicodePage, re.S)  # 获取当前页面的Table
        for nameinfo in novelsList:
            # print nameinfo
            # nameinfo = novelsList[0]
            novelurl = re.findall(r'<td align="left"><a href="(.*?)".*?</td>', nameinfo, re.S)  # 小说地址
            print novelurl
            info = re.findall(r'target="_blank">(.*?)</a>', nameinfo, re.S)  # 小说地址
            name = info[0]
            author = info[2]
            # print name + "-" + author
            # return ""
            if novelurl is not None:
                yield Request(str(novelurl[0]), dont_filter=True, callback=self.get_novelcontent, meta={'name': name,'author':author})

    def get_novelcontent(self, response):
        # print response.body
        novel_name = response.meta['name']  # 小说名字
        author = response.meta['author']  # 小说作者
        novelurl = response.url  # 小说地址
        # print novelurl
        click_num_total = response.xpath('//tr[1]/td[1]/text()').extract_first()  # 点击
        click_num_total = int(click_num_total.split("：")[1])
        # print click_num_total
        collect_num_total = response.xpath('//tr[1]/td[2]/text()').extract_first()  # 收藏
        collect_num_total = int(collect_num_total.split("：")[1])
        # print collect_num_total
        click_num_month = response.xpath('//tr[1]/td[3]/text()').extract_first()  # 收藏
        click_num_month = int(click_num_month.split("：")[1])*4
        # print click_num_month

        serialnumber = response.xpath('//tr[1]/td[4]/text()').extract_first()  # 连载字数
        serialnumber = int(serialnumber.split("：")[1])
        # print serialnumber
        # category = response.xpath('//div[@class="title"]/i[2]/text()').extract_first()  # 小说类别
        serialstatus = response.xpath('//div[@class="title"]/i[2]/text()').extract_first()  # 小说类别
        # print category
        category = response.xpath('//div[@class="title"]/a[2]/text()').extract_first()  # 状态
        # print serialstatus

        targentcontent = XiaoshuoItem()
        targentcontent['novel_name'] = novel_name
        targentcontent['author'] = author
        targentcontent['novelurl'] = novelurl
        targentcontent['serialstatus'] = serialstatus
        targentcontent['serialnumber'] = serialnumber
        targentcontent['category'] = category
        targentcontent['collect_num_total'] = int(collect_num_total)
        targentcontent['click_num_total'] = int(click_num_total)
        targentcontent['click_num_month'] = int(click_num_month)
        # targentcontent['name_id'] = name_id
        # targentcontent['novel_breif'] = novel_breif
        yield targentcontent
        # return ""
        # print novel_name,author,novelurl,serialstatus,serialnumber,category,name_id,collect_num_total,click_num_total,chapterlisturl

