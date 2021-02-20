from bs4 import BeautifulSoup
import xlwt
import urllib.request,urllib.error
import re
import sqlite3

def main():
    url = "https://aiqicha.baidu.com/company_detail_29453261288626?tab=certRecord"
    html = askURL(url)
    print(html)

def askURL(url):
    head = {        #模拟浏览器头部信息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 85.0.4183.83Safari / 537.36"
    }

            #用户代理，告诉豆瓣服务器，我们是什么类型的机器，告诉浏览器我们可以接收什么水平的浏览器
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response =  urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)

    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)

        if hasattr(e,"reason"):
            print(e.reason)

    return  html


if __name__ == '__main__':
    main()