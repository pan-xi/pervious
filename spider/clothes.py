import urllib.request
import re
import os


def imageCrawler(url, topath):
    headers = {  # 模拟请求头
        "Accept": "application/jaon,text/javascript, */*;q=0.01",
        "X-Requested-With": "XMLHttpRequest",  # 请求对象类型
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"  # 链接类型

    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    HtmlStr = response.read().decode("utf-8")  # 写入文件的时候先不要用decode会乱码
    # 因为没有decode所以打开要用wb的方式
    # with open(r"C:\Users\我爱陆地\PycharmProjects\爬虫简介与json\爬虫\image\yhd.html","wb")as f:
    #     f.write(HtmlStr)
    pat = r'<img (src="//(.*?)"/)|(original="//(.*?)" /)>'  # 一定要注意正则表达式与网页源代码格式一致，真尼玛坑爹一号店
    # img src="//img20.360buyimg.com/n7/s230x230_jfs/t1/84056/39/12179/451596/5d983a70E1f2e6714/b5636d18b127abd8.png!cc_230x230.jpg"/>
    # img original="//img14.360buyimg.com/n7/s230x230_jfs/t1/94747/2/9343/155285/5e0d66d6E57cb50c6/7c018557e0141e1f.jpg!cc_230x230.jpg" />
    re_image = re.compile(pat)  # 如果需要的话加re.S
    imagesList = re_image.findall(HtmlStr)
    # print(imagesList)
    # print(len(imagesList))
    #print(imagesList[1])
    #http://img.yihaodianimg.com/front-homepage/index/images/qryhd.png?1=1%22%20alt=%22APP%E6%9B%B4%E4%BC%98%E6%83%A0%E4%BA%8C%E7%BB%B4%E7%A0%81
    num = 0
    for i in imagesList:
        path = os.path.join(topath, str(num) + ".jpg")

        if num<12 :
            print(str(num)+" http://"+i[1])
        # 把图片下载到本地
            # 重要的事情说三遍：第一遍：一定要注意下面的方法里面网址是正确的，如果报错找不到host
            # 一定是爬到的网址不是所有的规律都一样的，需要分类，因为坑爹的网站不严谨
            urllib.request.urlretrieve(" http://"+i[1], filename=path)
        elif num>29:
            #print(str(num)+str(i[1].split('" alt="')[0]))
            # 重要的事情说三遍：第二遍：一定要注意下面的方法里面网址是正确的，如果报错找不到host
            # 一定是爬到的网址不是所有的规律都一样的，需要分类，因为坑爹的网站不严谨
            urllib.request.urlretrieve("http://"+i[1].split('" alt="')[0],filename=path)
        else:
            print(str(num)+" http://"+i[3])
            # 重要的事情说三遍：第三遍：一定要注意下面的方法里面网址是正确的，如果报错找不到host
            # 一定是爬到的网址不是所有的规律都一样的，需要分类，因为坑爹的网站不严谨
            urllib.request.urlretrieve(" http://"+i[3], filename=path)
            #http://img20.360buyimg.com/n7/s230x230_jfs/t1/94747/2/9343/155285/5e0d66d6E57cb50c6/7c018557e0141e1f.jpg!cc_230x230.jpg
        num += 1


# http://img30.360buyimg.com/n7/s230x230_jfs/t1/99329/10/11617/327663/5e3ad4bdE173522e1/9c9c979d9ebe7b66.jpg!cc_230x230.jpg

url = "http://search.yhd.com/c0-0/k%25E5%25A5%25B3%25E8%25A3%2585/"
topath = r"C:\Users\我爱陆地\PycharmProjects\爬虫简介与json\爬虫\image"
imageCrawler(url, topath)
