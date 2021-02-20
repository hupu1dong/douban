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

print('test5运行：')
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
options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55"')
url='https://isisn.nsfc.gov.cn/egrantindex/funcindex/prjsearch-list'
driver=webdriver.Firefox(executable_path='D:\driver\geckodriver.exe',options=options) # firefox版本：80
driver.maximize_window()
driver.get(url)
# driver.implicitly_wait(10) #隐式等待10秒
acodes = ['A01.数学', 'A02.力学', 'A03.天文学', 'A04.物理学Ⅰ', 'A05.物理学Ⅱ', 'A06.NSFC-中物院联合基金', 'A08.大科学装置联合基金', 'A09.天文联合基金',
          'B01.合成化学','B02.催化剂与表界面化学','B03.化学理论与机制','B04.化学测量学','B05.材料化学与能源化学','B06.环境化学','B07.化学生物学','B08.化学工程与工业化学',
          'C01.微生物学','C02.植物学','C03.生态学','C04.动物学','C05.生物物理与生物化学','C06.遗传学与生物信息学','C07.细胞生物学','C08.免疫学','C09.神经科学与心理学',
          'C10.生物材料、成像与组织工程学','C11.生理学与整合生物学','C12.发育生物学与生殖生物学','C13.农学基础与作物学','C14.植物保护学','C15.园艺学与植物营养学','C16.林学与草地科学',
          'C17.畜牧学','C18.兽医学','C19.水产学','C20.食品科学','C21.分子生物学与生物技术',
          'D01.地理学','D02.地质学','D03.地球化学','D04.地球物理学和空间物理学','D05.大气科学','D06.海洋科学','D07.环境地球科学',
          'E01.金属材料','E02.无机非金属材料','E03.有机敲分子材料','E04.矿业与治金工程','E05.机械设计与制造','E06.工程热物理与能源利用','E07.电气科学与工程','E08.建筑与土木工程',
          'E09.水利工程','E10.环境工程','E11.海洋工程','E12.交通与运载工程','E13.新概念材料与材料共性科学',
          'F01.电子学与信息系统','F02.计算机科学','F03.自动化','F04.半导体科学与信息器件','F05.光学和光电子学','F06.人工智能','F07.交叉学科中的信息科学',
          'G01.管理科学与工程','G02.工商管理','G03.经济科学','G04.宏观管理与政策',
          'H01.呼吸系统','H02.循环系统','H03.消化系统','H04.生殖系统/围生医学/新生儿','H05.泌尿系统','H06.运动系统','H07.内分泌系统/代谢和营养支持','H08.血液系统','H09.神经系统和精神疾病',
          'H10.医学免疫学', 'H11.皮肤及其附属器', 'H12.眼科学', 'H13.鼻咽喉头颈科学', 'H14.口腔颅领面科学', 'H15.急症医学/创伤/烧伤/整形', 'H16.肿瘤学', 'H17.康复医学', 'H18.影像医学与生物医学工程',
          'H19.医学病原生物与感染', 'H20.检验医学', 'H21.特种医学', 'H22.放射医学', 'H23.法医学', 'H24.地方病学/职业病学', 'H25.老年医学', 'H26预防医学', 'H27.中医学', 'H28.中药学', 'H29.中西医结合', 'H30.药物学', 'H31.药理学',
          'J01.国家基础入才培养基金', 'J02.青少年及软课题', 'J03.重点实验室', 'J04.计划委主任基金',
          'L00.联合基金战略研究', 'L01.农业领域', 'L02.人口与健康领域', 'L03.资源与环境领域', 'L04新材料与先进制造领域', 'L05.电子信息领域', 'L06.生物多样性保护领域', 'L07.矿产资源综合利用与新材料领域', 'L08.水资源与矿产资源领域',
          'L09.矿产资源领域', 'L10.农业', 'L11.新能源新材料领域', 'L12.水产生物资源研究领域', 'L13.食品安全检测技术领域', 'L14.管理科学领域', 'L15.生物与农业领域',
          'M01.委办公室委主任基金', 'R10.国际合作局', 'R20.国际合作局', 'R30.国际合作局', 'R40.国际合作局', 'R50.国际合作局']
sel = driver.find_elements_by_xpath("//select[@id='f_grantCode']/option")   #0为空，1，2，10，11必须同时选择申请代码
sel2 = driver.find_elements_by_xpath("//select[@id='f_year']/option")
# 数据采集
f = open('newdata.xls', 'w+', encoding='utf-8_sig')
f.write('项目名称,批准金额,年度,起始日期,类型,申请代码,申请方向,项目批准号\n')
for i in range(1, len(sel)):
    for k in range(45,len(acodes)):
        try:
            driver.find_elements_by_xpath("//select[@id='f_year']/option")[2].click()
            seltext = sel[i].text
            print(seltext)
            sel[i].click()
            sleep(random.randint(1, 3))
            print('i:', i)
            print('k:', acodes[k])
            st = acodes[k]
            st1 = st[0:3]

            driver.find_element_by_id('f_subjectCode').clear()
            sleep(random.randint(1, 3))
            driver.find_element_by_id('f_subjectCode').send_keys(st1)
            sleep(random.randint(1, 3))
            nele_locator = "//div[@class='ac_results']"
            nparam = (By.XPATH, nele_locator)
            try:
                while WebDriverWait(driver, 3).until(EC.visibility_of_element_located(nparam)):
                    ActionChains(driver).send_keys(Keys.ENTER).perform()
            except TimeoutException as e:
                pass

        except Exception as e:
            print(e)
            continue
        sleep(1)
        # 验证码操作
        code_tesseract("img_checkcode", "f_checkcode")

        # 搜索确定
        driver.find_element_by_id('searchBt').click()
        # try:
        #     driver.find_element_by_id('searchBt').click()
        # except Exception as e:
        #     print(e)
        #     continue
        ele_locator = "scmtip_content"
        param = (By.ID, ele_locator)
        try:
            while WebDriverWait(driver, 3).until(EC.visibility_of_element_located(param)):
                # qqq = driver.find_element_by_id('f_subjectCode')
                # # 对定位到的元素执行鼠标双击操作
                # ActionChains(driver).double_click(qqq).perform()
                # driver.find_element_by_id('f_subjectCode').click()
                # ActionChains(driver).send_keys(Keys.ENTER).perform()
                # # driver.find_elements_by_xpath("//select[@id='f_grantCode']/option")[i].click()
                # ielement = driver.find_element_by_id('img_checkcode')
                # driver.execute_script("arguments[0].click();", ielement)
                driver.find_element_by_id('img_checkcode').click()
                code_tesseract("img_checkcode", "f_checkcode")
                # sleep(1)
                driver.find_element_by_id('searchBt').click()
        except TimeoutException as e:
            pass

        # 数据采集

        # 页数获取
        try:
            op = driver.find_element_by_id('sp_1_dataBar').text
        except  Exception as e:
            print(e)
            continue
        if op == '':
            op = '0'
        elif ',' in op:
            op = op.replace(',', '')
        # print('op:'+op)
        page_sum = int(op)
        # print('page_sum:',page_sum)
        try:
            ol = driver.find_element_by_id('sp_2_dataBar').text
        except Exception as e:
            print()
            continue
        if ol == '':

            ol = '0'
        elif ',' in ol:
            ol = ol.replace(',', '')
        # print('ol:'+ol)
        list_sum = int(ol)
        # print('list_sum:',list_sum)
        if page_sum == 0 & list_sum == 0:
            try:
                driver.back()
            except Exception as e:
                print()
                continue

            # driver.refresh()
            sel = driver.find_elements_by_xpath("//select[@id='f_grantCode']/option")  # 0为空，1，2，10，11必须同时选择申请代码
            sel2 = driver.find_elements_by_xpath("//select[@id='f_year']/option")
            continue
        # # 数据采集
        # f = open('newdatas.xls', 'a+', encoding='utf-8_sig')
        # f.write('项目名称,批准金额,年度,起始日期,类型,申请代码,申请方向,项目批准号\n')
        for prow in range(page_sum):
            table = driver.find_element_by_id('dataGrid')
            table_rows = table.find_elements_by_tag_name('tr')
            print('第', prow+1,'页')
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
                try:
                    driver.find_element_by_id('next_dataBar').click()
                except  Exception as e:
                    print(e)
                    continue
                try:
                    while WebDriverWait(driver, 3).until(EC.visibility_of_element_located(param)):
                        # ielement = driver.find_element_by_id('img_checkcode')
                        # driver.execute_script("arguments[0].click();", ielement)
                        driver.find_element_by_id('img_checkcode').click()
                        code_tesseract("img_checkcode", "checkCode")
                        driver.find_element_by_id('next_dataBar').click()
                except TimeoutException as e:
                    pass
            sleep(random.randint(1, 5))

        else:
            try:
                driver.back()
            except Exception as e:
                print(e)
                continue
            # driver.refresh()
            sel = driver.find_elements_by_xpath("//select[@id='f_grantCode']/option")  # 0为空，1，2，10，11必须同时选择申请代码
            sel2 = driver.find_elements_by_xpath("//select[@id='f_year']/option")
            sleep(random.randint(1, 5))
            # print(i)
            continue


    else:
        try:
            driver.back()
        except Exception as e:
            print(e)
            continue
        # driver.refresh()
        sel = driver.find_elements_by_xpath("//select[@id='f_grantCode']/option")  # 0为空，1，2，10，11必须同时选择申请代码
        sel2 = driver.find_elements_by_xpath("//select[@id='f_year']/option")
        sleep(random.randint(1, 5))

else:
    driver.quit()
    f.close()
    print("抓取完毕！！")
elocaltime = time.asctime( time.localtime(time.time()) )
print ("截取时间为 :", elocaltime)