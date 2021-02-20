from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from time import sleep
from PIL import Image
import pytesseract # pip install pytesseract

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

url='https://isisn.nsfc.gov.cn/egrantindex/funcindex/prjsearch-list'
driver=webdriver.Firefox(executable_path='D:\driver\geckodriver.exe') # firefox版本：80
driver.maximize_window()
driver.get(url)

sel = driver.find_elements_by_xpath("//select[@id='f_grantCode']/option")   #0为空，1，2，10，11必须同时选择申请代码
sel2 = driver.find_elements_by_xpath("//select[@id='f_year']/option")
for i in range(3,len(sel)-10):
    for j in range(0,len(sel2)):
        sel[i].click()
        print('i:',i)
        sel2[j].click()
        print('j:',j)
        # 验证码操作
        code_tesseract("img_checkcode", "f_checkcode")

        # 搜索确定
        driver.find_element_by_id('searchBt').click()
        ele_locator = "scmtip_content"
        param = (By.ID, ele_locator)
        try:
            while WebDriverWait(driver, 3).until(EC.visibility_of_element_located(param)):
                driver.find_element_by_id('img_checkcode').click()
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
            op = op.replace(',','')
        print('op:'+op)
        page_sum = int(op)
        print('page_sum:',page_sum)
        ol = driver.find_element_by_id('sp_2_dataBar').text
        if ol == '':

            ol = '0'
        elif ',' in ol:
            ol = ol.replace(',','')
        print('ol:'+ol)
        list_sum = int(ol)
        print('list_sum:',list_sum)
        if page_sum == 0 & list_sum ==0:
            driver.back()
            driver.refresh()
            sel = driver.find_elements_by_xpath("//select[@id='f_grantCode']/option")  # 0为空，1，2，10，11必须同时选择申请代码
            sel2 = driver.find_elements_by_xpath("//select[@id='f_year']/option")
            continue
        # 数据采集
        f = open('data3.csv', 'w', encoding='utf-8')
        f.write('prjNo,subjectCode,ctitle,psnName,orgName,totalAmt,startEndDate\n')
        for prow in range(page_sum):
            table = driver.find_element_by_id('dataGrid')
            table_rows = table.find_elements_by_tag_name('tr')
            print('prow:',prow)
            for row in range(1, len(table_rows)):
                prjNo = table_rows[row].find_elements_by_tag_name('td')[1].text
                subjectCode = table_rows[row].find_elements_by_tag_name('td')[2].text
                ctitle = table_rows[row].find_elements_by_tag_name('td')[3].text
                psnName = table_rows[row].find_elements_by_tag_name('td')[4].text
                orgName = table_rows[row].find_elements_by_tag_name('td')[5].text
                totalAmt = table_rows[row].find_elements_by_tag_name('td')[6].text
                startEndDate = table_rows[row].find_elements_by_tag_name('td')[7].text
                f.write(f'{prjNo},{subjectCode},{ctitle},{psnName},{orgName},{totalAmt},{startEndDate}\n')
                print('row:',row)
            if prow != page_sum - 1:
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
            # else:
            #
            #     driver.back()
            #     driver.refresh()
            #     sel = driver.find_elements_by_xpath("//select[@id='f_grantCode']/option")  # 0为空，1，2，10，11必须同时选择申请代码
            #     sel2 = driver.find_elements_by_xpath("//select[@id='f_year']/option")
            #     continue

        else:
            driver.back()
            driver.refresh()
            sel = driver.find_elements_by_xpath("//select[@id='f_grantCode']/option")  # 0为空，1，2，10，11必须同时选择申请代码
            sel2 = driver.find_elements_by_xpath("//select[@id='f_year']/option")
            print(i)
            continue

    else:
        driver.back()
        driver.refresh()
        sel = driver.find_elements_by_xpath("//select[@id='f_grantCode']/option")  # 0为空，1，2，10，11必须同时选择申请代码
        sel2 = driver.find_elements_by_xpath("//select[@id='f_year']/option")





        # if driver.find_element_by_id('sp_1_dataBar').text != "":
        # page_sum = int(driver.find_element_by_id('sp_1_dataBar').text.strip())
        # print(driver.find_element_by_id('sp_1_dataBar').text.strip())
        # list_sum = int(driver.find_element_by_id('sp_2_dataBar').strip().text)
        # print(driver.find_element_by_id('sp_2_dataBar').text.strip())
        # if list_sum == 0 | page_sum == 0:
        #     driver.back()
        #     break
        # if page_sum > 0 | list_sum >0:
        #     driver.back()
        #     driver.refresh()
        #     sel = driver.find_elements_by_xpath("//select[@id='f_grantCode']/option")  # 0为空，1，2，10，11必须同时选择申请代码
        #     sel2 = driver.find_elements_by_xpath("//select[@id='f_year']/option")
        #     continue


        # else:
        #     driver.back()
        #     driver.refresh()
        #     sel = driver.find_elements_by_xpath("//select[@id='f_grantCode']/option")  # 0为空，1，2，10，11必须同时选择申请代码
        #     sel2 = driver.find_elements_by_xpath("//select[@id='f_year']/option")
        #     continue
    # driver.back()

driver.quit()
print("恭喜你运行成功！！！")