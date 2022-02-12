import urllib.request
import ssl
import re
import os
from collections import deque


def writeFileBytes(htmlBytes, topath):
    with open(topath, "wb")as f:
        f.write(htmlBytes)


def writerFileStr(htmlBytes, topath):
    with open(topath, "w")as f:
        f.write(str(htmlBytes))  # 搞不清上面编码就str


def getHtmlBytes(url):
    headers = {  # 模拟请求头
        "Accept": "application/jaon,text/javascript, */*;q=0.01",
        "X-Requested-With": "XMLHttpRequest",  # 请求对象类型
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"  # 链接类型

    }
    req = urllib.request.Request(url, headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    return response.read()


def qqCrawler(url, topath):
    htmlBytes = getHtmlBytes(url)
    # writeFileBytes(htmlBytes,r"C:\Users\我爱陆地\PycharmProjects\爬虫简介与json\爬虫\爬QQ号\qqFile1.html")
    # writerFileStr(htmlBytes,r"C:\Users\我爱陆地\PycharmProjects\爬虫简介与json\爬虫\爬QQ号\qqFile2.txt")
    # 到这里说明趴下了没问题
    htmlStr = str(htmlBytes)

    pat=r"[1-9]\d{4,9}"
    re_qq=re.compile(pat)
    qqsList=re_qq.findall(htmlStr)
    qqsList=list(set(qqsList))#去重复
    f=open(topath,"a")
    for qqStr in qqsList:
        f.write(qqStr+"\n")
        f.flush()
    f.close()

    # print(qqsList)
    # print(len(qqsList))

    #最全网址的正则表达式
    # pat = r'((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0,9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\$%_\./-~-]*)?'
    pat = r'(((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?)'
    re_url=re.compile(pat)
    urlList=re_url.findall(htmlStr)
    urlList=list(set(urlList))
    # print(urlList)
    # print(len(urlList))
    return urlList



def center(url,topath):
    queue=deque()
    queue.append(url)
    try:
        while len(queue)!=0:
            targetUrl=queue.popleft()
            urlList=qqCrawler(targetUrl, topath)
            for item in urlList:
                tempUrl=item[0]
                queue.append(tempUrl)
    except:
        return 0


url = "https://www.douban.com/group/topic/17359302/"
topath = r"C:\Users\我爱陆地\PycharmProjects\爬虫简介与json\爬虫\爬QQ号(还有网址正则表达式)\qqFile.txt"
center(url,topath)

