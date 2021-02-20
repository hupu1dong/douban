from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time,datetime
from time import sleep
from PIL import Image
import pytesseract # pip install pytesseract
import random

slocaltime = time.asctime( time.localtime(time.time()) )
print ("程序开始时间为时间为 :", slocaltime)
def code_tesseract(img_checkcode,checkcode):
    driver.save_screenshot('html.png')
    yzm=driver.find_element_by_id(img_checkcode)
    location=yzm.location#获取验证码x,y轴坐标
    size=yzm.size#获取验证码的长宽
    k = 1.25
    rangle=(int(location['x'])*k,int(location['y'])*k,int(location['x']+size['width'])*k,int(location['y']+size['height'])*k)#截取的位置坐标
    i=Image.open("html.png") #打开截图
    frame4=i.crop(rangle) #使用Image的crop函数，从截图中再次截取我们需要的区域
    frame4.save('code.png')#将截取到的验证码保存为jpg图片
    text = pytesseract.image_to_string(Image.open("code.png")).strip()
    # print(text)
    driver.find_element_by_id(checkcode).clear()
    driver.find_element_by_id(checkcode).send_keys(text)
options = webdriver.FirefoxOptions()
# options.add_argument("--proxy-server=http://1.196.177.213:9999")
options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69"')
url='https://isisn.nsfc.gov.cn/egrantindex/funcindex/prjsearch-list'
driver=webdriver.Firefox(executable_path='D:\driver\geckodriver.exe',options=options) # firefox版本：80
driver.maximize_window()
driver.get(url)
sel = driver.find_elements_by_xpath("//select[@id='f_grantCode']/option")   #0为空，1，2，10，11必须同时选择申请代码
sel2 = driver.find_elements_by_xpath("//select[@id='f_year']/option")
sel2[2].click()
si = driver.find_element_by_xpath("//a[@id='f_subjectCode_img']")
nc = driver.find_elements_by_xpath("//div[@id='f_subjectCode_treeId']/li/button")
nc2 = driver.find_elements_by_xpath("//div[@id='f_subjectCode_treeId']/li//ul/li//span")
#45 E02.无机非金属材料
for i in range(1, len(sel)):
    for n1 in range(len(nc)):
        for n2 in range(len(nc2)):
            seltext = sel[i].text
            print(seltext)
            sel[i].click()
            sleep(random.randint(1, 5))
            print('i:', i)
            si.click()
            sleep(0.5)
            nc[n1].click()
            print('n1:',n1)
            nc2[n2].click()
            sleep(0.5)
            print('n2:',n2)
            st = nc[n2].text
            print(nc[n2].text)
            # 验证码操作
            code_tesseract("img_checkcode", "f_checkcode")

            # 搜索确定
            driver.find_element_by_id('searchBt').click()
            ele_locator = "scmtip_content"
            param = (By.ID, ele_locator)
            try:
                while WebDriverWait(driver, 3).until(EC.visibility_of_element_located(param)):
                    ielement = driver.find_element_by_id('img_checkcode')
                    driver.execute_script("arguments[0].click();", ielement)
                    # driver.find_element_by_id('img_checkcode').click()
                    code_tesseract("img_checkcode", "f_checkcode")
                    # sleep(1)
                    driver.find_element_by_id('searchBt').click()
            except TimeoutException as e:
                pass

            # 数据采集

            # 页数获取
            op = driver.find_element_by_id('sp_1_dataBar').text
            if op == '':
                op = '0'
            elif ',' in op:
                op = op.replace(',', '')
            # print('op:'+op)
            page_sum = int(op)
            # print('page_sum:',page_sum)
            ol = driver.find_element_by_id('sp_2_dataBar').text
            if ol == '':

                ol = '0'
            elif ',' in ol:
                ol = ol.replace(',', '')
            # print('ol:'+ol)
            list_sum = int(ol)
            # print('list_sum:',list_sum)
            if page_sum == 0 & list_sum == 0:
                driver.back()
                # driver.refresh()
                sel = driver.find_elements_by_xpath("//select[@id='f_grantCode']/option")
                si = driver.find_element_by_xpath("//a[@id='f_subjectCode_img']")
                nc = driver.find_elements_by_xpath("//div[@id='f_subjectCode_treeId']/li/button")
                nc2 = driver.find_elements_by_xpath("//div[@id='f_subjectCode_treeId']/li//ul/li//span")
                continue
            # 数据采集
            f = open('data10.xls', 'a+', encoding='utf-8_sig')
            # 项目名称
            # f.write('prjNo,subjectCode,ctitle,psnName,orgName,totalAmt,startEndDate\n')
            f.write('项目名称,批准金额,年度,起始日期,类型,申请代码,申请方向,项目批准号\n')
            for prow in range(page_sum):
                table = driver.find_element_by_id('dataGrid')
                table_rows = table.find_elements_by_tag_name('tr')
                print('prow:', prow)
                # sel[i].text
                for row in range(1, len(table_rows)):
                    prjNo = table_rows[row].find_elements_by_tag_name('td')[1].text
                    subjectCode = table_rows[row].find_elements_by_tag_name('td')[2].text
                    ctitle = table_rows[row].find_elements_by_tag_name('td')[3].text
                    psnName = table_rows[row].find_elements_by_tag_name('td')[4].text
                    orgName = table_rows[row].find_elements_by_tag_name('td')[5].text
                    totalAmt = table_rows[row].find_elements_by_tag_name('td')[6].text
                    startEndDate = table_rows[row].find_elements_by_tag_name('td')[7].text
                    f.write(f'{ctitle},{totalAmt},{"2018"},{startEndDate},{seltext},{subjectCode},{st[4:]},{prjNo}\n')
                    # f.write(f'{prjNo},{subjectCode},{ctitle},{psnName},{orgName},{totalAmt},{startEndDate}\n')
                    # print('row:',row)
                if prow != page_sum - 1:
                    # 验证码操作
                    code_tesseract("img_checkcode", "checkCode")
                    # 点击下一页
                    driver.find_element_by_id('next_dataBar').click()
                    try:
                        while WebDriverWait(driver, 3).until(EC.visibility_of_element_located(param)):
                            ielement = driver.find_element_by_id('img_checkcode')
                            driver.execute_script("arguments[0].click();", ielement)
                            # driver.find_element_by_id('img_checkcode').click()
                            code_tesseract("img_checkcode", "checkCode")
                            driver.find_element_by_id('next_dataBar').click()
                    except TimeoutException as e:
                        pass
                sleep(random.randint(5, 20))

            else:
                driver.back()
                # driver.refresh()
                sel = driver.find_elements_by_xpath("//select[@id='f_grantCode']/option")  # 0为空，1，2，10，11必须同时选择申请代码
                si = driver.find_element_by_xpath("//a[@id='f_subjectCode_img']")
                nc = driver.find_elements_by_xpath("//div[@id='f_subjectCode_treeId']/li/button")
                nc2 = driver.find_elements_by_xpath("//div[@id='f_subjectCode_treeId']/li//ul/li//span")
                sleep(random.randint(5, 20))
                # print(i)
                continue


        else:
            driver.back()
            # driver.refresh()
            sel = driver.find_elements_by_xpath("//select[@id='f_grantCode']/option")  # 0为空，1，2，10，11必须同时选择申请代码
            si = driver.find_element_by_xpath("//a[@id='f_subjectCode_img']")
            nc = driver.find_elements_by_xpath("//div[@id='f_subjectCode_treeId']/li/button")
            nc2 = driver.find_elements_by_xpath("//div[@id='f_subjectCode_treeId']/li//ul/li//span")
            sleep(random.randint(5, 20))

    else:
        driver.back()
        # driver.refresh()
        sel = driver.find_elements_by_xpath("//select[@id='f_grantCode']/option")  # 0为空，1，2，10，11必须同时选择申请代码
        # si = driver.find_element_by_xpath("//a[@id='f_subjectCode_img']")
        nc = driver.find_elements_by_xpath("//div[@id='f_subjectCode_treeId']/li/button")
        # nc2 = driver.find_elements_by_xpath("//div[@id='f_subjectCode_treeId']/li//ul/li//span")
        sleep(random.randint(5, 20))

else:
    driver.quit()
    print("抓取完毕！！")
elocaltime = time.asctime( time.localtime(time.time()) )
print ("截取时间为 :", elocaltime)