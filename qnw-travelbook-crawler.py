# -*- coding: utf-8 -*-
"""
Created on Fri May 29 10:56:37 2020

@author: admin
"""
import re
import requests
from lxml import etree
import time
import random

class qnw_crawler:
    def __init__(self):
        self.ip = ['27.188.62.3','218.203.132.117','116.22.31.32','101.231.104.82','223.68.190.130','113.121.94.227','175.165.128.131','218.14.108.53','117.89.25.75','183.162.166.160','61.145.48.179']  
        #url = "https://www.mafengwo.cn/gonglve/ziyouxing/243835.html?cid=1010616"
        self.headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4100.3 Safari/537.36"} 
        self.user_agent = [
               "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
               "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
               "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
               "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
               "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
               "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
               "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
               "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
               "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
               "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
               "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
               "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
               "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
               "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
               "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4100.3 Safari/537.36"
               ]
    def get_content(self):
        u = open('D:/Desktop/明寰科技/去哪儿爬虫/bj_url.txt','r')
        for url in u:   
            headers = {"User-Agent":random.choice(self.user_agent)}
            proxies = {'http':random.choice(self.ip)}
            response = requests.get(url,headers=headers,proxies=proxies)
            content = response.content.decode('utf8')
            html = etree.HTML(content)
            text = html.xpath('//div[@class="b_panel_schedule"]/div//text()')
            title = html.xpath('//div[@class="user_info"]/div[@class="e_title clrfix"]/h1/span/text()')
            title_new = re.sub('[\W_]+','',title[0])
            try:
                with open('D:/Desktop/明寰科技/去哪儿游记/北京/{}.txt'.format(title_new),'w+',encoding='utf-8') as f:
                    for line in text:
                        f.write(line+'\n')
                f.close()
                print('{}.txt'.format(title_new)+'************已爬完')
                time.sleep(random.randint(35,45))
            except:
                with open('D:/Desktop/明寰科技/去哪儿爬虫/problem_url.txt','w+',encoding='utf-8') as p:
                    p.write(url+'\n')
                p.close()
        u.close()

if __name__ == '__main__':
    spider = qnw_crawler()
    result = spider.get_content()            
            
            

