from bs4 import BeautifulSoup
import xlwt
import urllib.request,urllib.error
import re
import sqlite3

def main():
    baseurl = "https://isisn.nsfc.gov.cn/egrantindex/funcindex/prjsearch-list?locale=zh_CN"
    datalist = getData(baseurl)
    html = askURL(baseurl)
    print(html)


def getData(baseurl):
    datalist = []







#得到指定一个URL的网页内容
def askURL(url):
    head = {        #模拟浏览器头部信息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63"

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
#保存数据
def saveData(datalist,savepath):
    print("save....")






if __name__ == "__main__":
    main()
    # init_db("movietest.db")
    print("爬取完毕！！！")