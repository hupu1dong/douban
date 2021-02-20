from bs4 import BeautifulSoup
import xlwt
import urllib.request,urllib.error
import re
import sqlite3

def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)

    # savepath = ".\\豆瓣电影Top250.xls"
    dbpath = "movie.db"
    saveData2DB(datalist,dbpath)

    # saveData(datalist,savepath)

    # askURL("https://movie.douban.com/top250?start=")
    #链接规则
findLink = re.compile(r'<a href="(.*?)">') #创建正则表达式对象，表示规则(字符串模式）
#图片
findImg = re.compile(r'img.*src="(.*?)"',re.S)  #让换行符在字符中
#片名
findTitle = re.compile(r'<span class="title">(.*?)</span>')
#影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
#评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#概况
findInq = re.compile(r'<span class="inq">(.*?)</span>')
#找到影片的相关内容
findContent = re.compile(r'<p class="">(.*?)</p>',re.S)
#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):
         url = baseurl + str(i*25)
         html = askURL(url) #保存获取到的网页源码
         # 逐一解析数据
         soup = BeautifulSoup(html, "html.parser")
         #  # 测试查看所有电影信息
         for item in soup.find_all('div', class_="item"):
             data = []  # 保存一部电影所有信息
             item = str(item)
             # print(item)
             # break
             # print(item)
             # 获取影片详情链接
             link = re.findall(findLink, item)[0]
             data.append(link)
             # print(link)
             Imgsrc = re.findall(findImg, item)[0]
             data.append(Imgsrc)
             # print(Imgsrc)

             Title = re.findall(findTitle, item)  # 片名可能只有一个中文名
             if (len(Title) == 2):
                 ctitle = Title[0]
                 data.append(ctitle)  # 中文名
                 otitle = Title[1].replace("/", "")  # 去掉无关字符
                 data.append(otitle)  # 外文名
             else:
                 data.append(Title[0])
                 data.append('   ')  # 外文名字留空

             rating = re.findall(findRating, item)[0]
             data.append(rating)  # 添加评分

             judge = re.findall(findJudge, item)[0]
             data.append(judge)  # 添加评价人数

             inq = re.findall(findInq, item)
             if len(inq) != 0:
                 inq = inq[0].replace("。", "")  # 去掉句号
                 data.append(inq)  # 添加概述
             else:
                 data.append("   ")  # 留空

             content = re.findall(findContent, item)[0]
             content = re.sub('<br(\s+)?/>(\s+)?', " ", content)  # 替换br
             content = re.sub('/', " ", content)  # 替换/
             data.append(content.strip())

             datalist.append(data)  # 把处理好的一部电影储存在datalist

    return datalist
             # print(datalist)






#得到指定一个URL的网页内容
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
#保存数据
def saveData(datalist,savepath):
    print("save....")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建book对象
    sheet = book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)  # 创建工作表
    col = ('电影详情链接',"图片链接","影片中文名","影片外国名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i]) #列名
    for i in range(0,250):
        print("第%d条"%(i+1))
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])

        book.save(savepath)

def saveData2DB(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()


    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"'+data[index]+'"'
        sql = '''
                insert into movie250 (
                info_link,pic_link,cname,ename,score,rated,instroduction,info)
                values (%s)'''%",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()

    cur.close()
    conn.close()


def init_db(dbpath):
    sql = '''
        create table movie250
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated numeric,
        instroduction text,
        info text
        )
    '''    #创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()




if __name__ == "__main__":
    main()
    # init_db("movietest.db")
    print("爬取完毕！！！")