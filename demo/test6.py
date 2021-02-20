from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from PIL import Image
import pytesseract # pip install pytesseract

def code_tesseract(img_checkcode,checkcode):
    driver.save_screenshot('html.png')
    yzm=driver.find_element_by_id(img_checkcode)
    location=yzm.location#获取验证码x,y轴坐标
    size=yzm.size#获取验证码的长宽
    k = 1.25    #我的电脑缩放比例为125%
    rangle=(int(location['x'])*k,int(location['y'])*k,int(location['x']+size['width'])*k,int(location['y']+size['height'])*k)#截取的位置坐标
    i=Image.open("html.png") #打开截图
    frame4=i.crop(rangle) #使用Image的crop函数，从截图中再次截取我们需要的区域
    frame4.save('code.png')#将截取到的验证码保存为jpg图片
    text = pytesseract.image_to_string(Image.open("code.png")).strip()
    print(text)
    driver.find_element_by_id(checkcode).clear()
    driver.find_element_by_id(checkcode).send_keys(text)
url='https://isisn.nsfc.gov.cn/egrantindex/funcindex/prjsearch-list'
driver=webdriver.Firefox(executable_path='D:\driver\geckodriver.exe') # firefox版本：80
driver.maximize_window()
driver.get(url)
#资助类别选择
sel = driver.find_element_by_id("f_grantCode")
sel.find_element_by_css_selector("option[value='649']").click()
gsel = sel.find_element_by_css_selector("option[value='649']").text

#年限选择
sel = driver.find_element_by_id("f_year")
sel.find_element_by_css_selector("option[value='2019']").click()
ysel = sel.find_element_by_css_selector("option[value='2019']").text
# 验证码操作
code_tesseract("img_checkcode","f_checkcode")


#搜索确定
driver.find_element_by_id('searchBt').click()
ele_locator = "scmtip_content"
param = (By.ID,ele_locator)
try:
    while WebDriverWait(driver,3).until(EC.visibility_of_element_located(param)):
        driver.find_element_by_id('img_checkcode').click()
        code_tesseract("img_checkcode", "f_checkcode")
        driver.find_element_by_id('searchBt').click()
except TimeoutException as e:
    pass

# 数据采集

# 页数获取
page_sum=int(driver.find_element_by_id('sp_1_dataBar').text)
# 数据采集
f=open('data8.xls','w',encoding='utf-8_sig')
# f.write('prjNo,subjectCode,ctitle,psnName,orgName,totalAmt,startEndDate\n')
f.write('项目名称,批准金额,年度,起始日期,类型,申请代码,项目批准号\n')
for i in range(page_sum):
    table=driver.find_element_by_id('dataGrid')
    table_rows=table.find_elements_by_tag_name('tr')
    for row in range(1,len(table_rows)):
        prjNo=table_rows[row].find_elements_by_tag_name('td')[1].text
        subjectCode=table_rows[row].find_elements_by_tag_name('td')[2].text
        ctitle=table_rows[row].find_elements_by_tag_name('td')[3].text
        psnName=table_rows[row].find_elements_by_tag_name('td')[4].text
        orgName=table_rows[row].find_elements_by_tag_name('td')[5].text
        totalAmt=table_rows[row].find_elements_by_tag_name('td')[6].text
        startEndDate=table_rows[row].find_elements_by_tag_name('td')[7].text
        f.write(f'{ctitle},{totalAmt},{ysel},{startEndDate},{gsel},{subjectCode},{prjNo}\n')
        # f.write(f'{prjNo},{subjectCode},{ctitle},{psnName},{orgName},{totalAmt},{startEndDate}\n')
    if i!=page_sum-1:
        # 验证码操作
        code_tesseract("img_checkcode", "checkCode")
        # 点击下一页
        driver.find_element_by_id('next_dataBar').click()
        try:
            while WebDriverWait(driver, 3).until(EC.visibility_of_element_located(param)):
                driver.find_element_by_id('img_checkcode').click()
                code_tesseract("img_checkcode", "checkCode")
                driver.find_element_by_id('next_dataBar').click()
        except TimeoutException as e:
            pass
driver.quit()