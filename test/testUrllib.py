import urllib.request
#GET请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))
import urllib.parse
#post请求
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode('utf-8'))

#超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=2)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("超时了哥们")


# response = urllib.request.urlopen("http://www.baidu.com",timeout=2)
# print(response.status)
# print(response.getheaders())
# print(response.getheader("Bdpagetype"))
# url = "https://www.douban.com"
url = "https://www.baidu.com"

# url = "http://httpbin.org/post"
# data = bytes(urllib.parse.urlencode({"name":"eric"}),encoding="utf-8")
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63"

}
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))