# qnw-spider
按目的地爬取去哪网的旅游攻略与景点信息

爬虫思路：

1、qnw-travelbook-geturl.py与qnw-spots-geturl.py爬取每个地区的所有旅游攻略、景点信息的网址，并按地区存储在不同文档

2、qnw-travelbook-crawler.py与qnw-spots-crawler.py逐行读取url文件并爬取具体信息，一篇旅游攻略为一个文档，一个城市的景点地址、介绍信息为一个文档

存在的问题：

获取旅游攻略url时，即使放慢速度在爬取1000个url后仍会出现封ip24小时的问题，目前只能采取轮换ip的方法
