'''
Created on 2018年2月8日

@author: zhengxiyang
'''
from bs4 import BeautifulSoup  
from urllib import request  
import queue 
import threading
import time
import urllib
from asyncio.tasks import sleep
from Test3 import soup
import json

def publicMethod(target_url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.4793.400 QQBrowser/10.0.745.400'}    
    req = request.Request(target_url,headers=headers)  
    response = request.urlopen(req)
    response = response.read().decode('utf8')
    soup = BeautifulSoup(response,'lxml')
    return soup
if __name__ == '__main__':  
    ''' http://www.myzaker.com/channel/660'#660是Zaker的热点频道
      <a class="nav_item nav_item_active" data-appid="660" href="//www.myzaker.com/channel/660" title="热点新闻">热点</a>
<a class="nav_item " data-appid="9" href="//www.myzaker.com/channel/9" title="娱乐新闻">娱乐</a>
<a class="nav_item " target="_blank" data-appid="7" href="//www.myzaker.com/channel/7" title="汽车新闻">汽车</a>
<a class="nav_item " data-appid="8" href="//www.myzaker.com/channel/8" title="体育新闻">体育</a>
<a class="nav_item " target="_blank" data-appid="13" href="//www.myzaker.com/channel/13" title="科技新闻">科技</a>
<a class="nav_item " data-appid="1" href="//www.myzaker.com/channel/1" title="国内新闻">国内</a>
<a class="nav_item " data-appid="2" href="//www.myzaker.com/channel/2" title="国际新闻">国际</a>
<a class="nav_item " data-appid="3" href="//www.myzaker.com/channel/3" title="军事新闻">军事</a>
<a class="nav_item " data-appid="4" href="//www.myzaker.com/channel/4" title="财经新闻">财经</a>
<a class="nav_item " data-appid="5" href="//www.myzaker.com/channel/5" title="互联网新闻">互联网</a>
<a class="nav_item " data-appid="11" href="//www.myzaker.com/channel/11" title="教育新闻">教育</a>  
<a class="nav_menu_item" href="//www.myzaker.com/channel/12" data-appid="12" title="时尚新闻">时尚</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/14" data-appid="14" title="社会新闻">社会</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/959" data-appid="959" title="亲子新闻">亲子</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/981" data-appid="981" title="旅游新闻">旅游</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/1039" data-appid="1039" title="科学新闻">科学</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/1014" data-appid="1014" title="星座新闻">星座</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/1067" data-appid="1067" title="奢侈品新闻">奢侈品</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10376" data-appid="10376" title=" 游戏新闻"> 游戏</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10386" data-appid="10386" title="美食新闻">美食</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10530" data-appid="10530" title="电影新闻">电影</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10802" data-appid="10802" title="健康新闻">健康</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/11195" data-appid="11195" title="理财新闻">理财</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10089" data-appid="10089" title="保定新闻">保定</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10161" data-appid="10161" title="长春新闻">长春</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/12183" data-appid="12183" title="触电新闻">触电</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10146" data-appid="10146" title="长沙新闻">长沙</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10192" data-appid="10192" title="大连新闻">大连</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10076" data-appid="10076" title="贵阳新闻">贵阳</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10045" data-appid="10045" title="广州新闻">广州</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10119" data-appid="10119" title="哈尔滨新闻">哈尔滨</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10011" data-appid="10011" title="合肥新闻">合肥</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10046" data-appid="10046" title="河源新闻">河源</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10034" data-appid="10034" title="兰州新闻">兰州</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10184" data-appid="10184" title="南昌新闻">南昌</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10169" data-appid="10169" title="南京新闻">南京</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10070" data-appid="10070" title="南宁新闻">南宁</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10095" data-appid="10095" title="秦皇岛新闻">秦皇岛</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10096" data-appid="10096" title="石家庄新闻">石家庄</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/12659" data-appid="12659" title="沈阳新闻">沈阳</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10055" data-appid="10055" title="深圳新闻">深圳</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10304" data-appid="10304" title="台州新闻">台州</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10140" data-appid="10140" title="武汉新闻">武汉</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10028" data-appid="10028" title="厦门新闻">厦门</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10114" data-appid="10114" title="郑州新闻">郑州</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10061" data-appid="10061" title="珠海新闻">珠海</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10000" data-appid="10000" title="北京新闻">北京</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10003" data-appid="10003" title="重庆新闻">重庆</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10260" data-appid="10260" title="成都新闻">成都</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10008" data-appid="10008" title="池州新闻">池州</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10043" data-appid="10043" title="东莞新闻">东莞</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10021" data-appid="10021" title="福州新闻">福州</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10044" data-appid="10044" title="佛山新闻">佛山</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10296" data-appid="10296" title="杭州新闻">杭州</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10224" data-appid="10224" title="济南新闻">济南</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10225" data-appid="10225" title="济宁新闻">济宁</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10288" data-appid="10288" title="昆明新闻">昆明</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10050" data-appid="10050" title="梅州新闻">梅州</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10106" data-appid="10106" title="南阳新闻">南阳</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10107" data-appid="10107" title="平顶山新闻">平顶山</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10229" data-appid="10229" title="青岛新闻">青岛</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10026" data-appid="10026" title="泉州新闻">泉州</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10001" data-appid="10001" title="上海新闻">上海</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10231" data-appid="10231" title="泰安新闻">泰安</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10002" data-appid="10002" title="天津新闻">天津</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10040" data-appid="10040" title="武威新闻">武威</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10232" data-appid="10232" title="威海新闻">威海</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10233" data-appid="10233" title="潍坊新闻">潍坊</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10254" data-appid="10254" title="西安新闻">西安</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10234" data-appid="10234" title="烟台新闻">烟台</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10060" data-appid="10060" title="中山新闻">中山</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10029" data-appid="10029" title="漳州新闻">漳州</a>
<a class="nav_menu_item" href="//www.myzaker.com/channel/10236" data-appid="10236" title="淄博新闻">淄博</a>
    '''
    channelUrlList = ['http://www.myzaker.com/channel/660','http://www.myzaker.com/channel/9']#频道list
    channelUrl = queue.Queue()#频道队列
    nextPageUrl=queue.Queue()#下一页列表地址
    for i in channelUrlList:
        channelUrl.put(i)
        channelUrl.task_done()

#线程1 获取每个频道列表第一页新闻 与nextUrl
class getListNews(threading.Thread):
    def __init__(self,channelUrl):
        threading.Thread.__init__(self)
        self.channelUrl = channelUrl
    def run(self):
        while(True):
            channel = channelUrl.get()
            soup = publicMethod(channel)
            NewsList = soup.findAll('a',class_='img')
            nextUrl = soup.find('input',id='nexturl')
            nextUrl=nextUrl.get("value")#获取下一个爬取的地址
            nextUrl=urllib.parse.unquote(nextUrl)
            nextUrl='http:'+nextUrl
            #print(nextUrl)
            nextPageUrl.put(nextUrl)
            nextPageUrl.task_done()
            for n in NewsList:
                title = n.get("title")
                imgurl = n.get("style")
                url = n.get("href")
                imgurl=imgurl.replace("background-image:url(//","").replace(");","")
                url=url.replace("/","",2)
                print(title+'----'+imgurl+'----'+url)
            if self.channelUrl.empty():
                print("队列中没有网址了")#队列中没有地址了 弹出方法防止抛出异常 （try ch） 
                break
t1 = getListNews(channelUrl)
t1.start()
#线程2 取到第一页的nexturl 分析 然后将其他接来的新闻列表文章以及nexturl取出
class getNextUrlAndNews(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True :
            if nextPageUrl.empty():
                sleep(5)#等一等线程1
            else :
                print("这里是线程2开始启动!")
                nextUrl=nextPageUrl.get()
                soup = publicMethod(nextUrl)
                jsonData= soup.text#json数据字符串化
                Dict=json.loads(jsonData)#转换为dict类型
                print(Dict)
                NewsHrefList=Dict.get("data").get("article")#list里面嵌套dict
                for News in NewsHrefList:
                    href = News.get("href")
                    print(href)
                    print(NewsHrefList)
#线程3
#线程4
