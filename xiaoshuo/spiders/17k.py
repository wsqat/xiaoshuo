# coding:utf-8
import scrapy
import re
from scrapy.http import Request
from xiaoshuo.items import XiaoshuoItem
from scrapy.selector import Selector
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2
import json

class SeventeenK(scrapy.Spider):
    name = "seventeen"
    allowed_domains = ["all.17k.com/"]
    # bash_url = "http://all.17k.com/lib/book/2_0_0_0_0_0_0_0_1.html?" #1
    base_url = "http://all.17k.com/lib/book/" #2_0_0_0_0_4_0_0_1
    #http://chuangshi.qq.com/bk/p/2.html
    # start_urls = ['http://all.17k.com/lib/book/2_0_0_0_0_0_0_0_%s.html?' % i for i in [1,200,400]]
    # start_urls = ['http://all.17k.com/lib/book/2_0_0_0_0_0_0_0_1.html?']

    def start_requests(self):
        # for i in range(1,11):
        # max_num = 7329 # 获取当前页面的最大页码数
        max_num = 500  # 获取当前页面的最大页码数
        print u"当前开始爬取17K小说网……"
        for i in range(2, 5):
            for j in range(1, int(max_num)+1):
            # for j in range(1, 2):
            #     print  "当前页数："+str(max_num)
                url = self.base_url + str(i) + "_0_0_0_0_4_0_0_" + str(j) + ".html?"
                # print url
                yield Request(url, dont_filter=True, callback=self.get_name)  # 将新的页面url的内容传递给get_name函数去处理
        # return ""

    def get_name(self, response):
        myPgae = response.body
        unicodePage = myPgae.decode('utf-8')
        # print  myPgae
        # # 根据正则表达式拿到所有的内容
        # novelsTable = re.findall(r'<ul class="main_con">(.*?)</ul>', unicodePage, re.S)  # 获取当前页面的Table
        # print novelsTable[0]
        novelsList = re.findall(r'<tr class=.*?>(.*?)</tr>', unicodePage, re.S)  # 获取当前页面的Table
        # print len(novelsList)
        # nameinfo = novelsList[0]
        for nameinfo in novelsList:
            # print nameinfo
            novelurl = re.findall(r'<a .*? href="(.*?)" target.*?', nameinfo, re.S)[0]
            # print novelurl
            info = re.findall(r'target="_blank".*?>(.*?)</a>', nameinfo, re.S)  # 小说地址
            category = info[0]
            novel_name = info[1]
            author = info[-1]
            # print novel_name+" "+ author + " " + category
            serialnumber = re.findall(r'<td class="td5">(.*?)</td>', nameinfo, re.S)[0]
            # print serialnumber
            serialstatus = re.findall(r'<em class="fc2">(.*?)</em>', nameinfo, re.S)[0]
            serialstatus = serialstatus.strip()
            targentcontent = XiaoshuoItem()
            targentcontent['novel_name'] = novel_name
            targentcontent['author'] = author
            targentcontent['novelurl'] = novelurl
            targentcontent['category'] = category
            targentcontent['serialnumber'] = serialnumber
            targentcontent['serialstatus'] = serialstatus
            # return ""
            # print targentcontent
            # novelurl = "http://www.17k.com/book/1893454.html"
            # print novelurl
            if novelurl is not None:
                yield Request(str(novelurl), dont_filter=True, callback=self.get_novelcontent, meta={'targentcontent': targentcontent})

    def get_novelcontent(self, response):
        url = response.url
        novelId = url.split("/")[-1].split(".")[0]
        # print novelId
        # http://api.ali.17k.com/v2/book/935571/stat_info?app_key=3362611833
        newurl = "http://api.ali.17k.com/v2/book/"+str(novelId)+"/stat_info?app_key=3362611833"
        req = urllib2.Request(newurl)
        # print req
        res_data = urllib2.urlopen(req)
        # res = res_data.read()
        res = json.load(res_data)
        click_num_total = res['data']['click_info']['total_count']
        click_num_month = res['data']['click_info']['month_count']
        # 鲜花作为总收藏数
        collect_num_total = res['data']['flower_info']['total_count']

        targentcontent = response.meta['targentcontent']
        print targentcontent
        targentcontent['click_num_total'] = int(click_num_total)
        targentcontent['collect_num_total'] = int(collect_num_total)
        targentcontent['click_num_month'] = int(click_num_month)

        # return ""
        yield targentcontent

