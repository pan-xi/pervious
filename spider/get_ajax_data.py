import urllib.request
import ssl
import json


# 用google chrome抓包时注意关闭代理！！！

def ajaxCrawler(url):
    headers = {  # 模拟请求头
        "Accept": "application/jaon,text/javascript, */*;q=0.01",
        "X-Requested-With": "XMLHttpRequest",  # 请求对象类型
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
    }  # 链接类型
    req = urllib.request.Request(url, headers=headers)
    # 使用ssl创建未验证的上下文（即免验证证书）（好像不需要了现在，有没有结果都一样，至少对于这个程序就是）
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    jsonStr = response.read().decode("utf-8")
    jsonData = json.loads(jsonStr)
    return jsonData


'''
url="https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=20&limit=20"
info=ajaxCrawler(url)
print(info)
'''
for i in range(1, 10):
    url = "https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=" + str(
        i * 20) + "&limit=20"
    info = ajaxCrawler(url)
    print(info)
    #print(len(info))
