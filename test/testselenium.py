from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from PIL import Image
import pytesseract # pip install pytesseract

# url='https://isisn.nsfc.gov.cn/egrantindex/funcindex/prjsearch-list'
# driver = webdriver.Firefox(executable_path='D:\driver\geckodriver.exe')


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
    print(text)
    driver.find_element_by_id(checkcode).clear()
    driver.find_element_by_id(checkcode).send_keys(text)

url='https://isisn.nsfc.gov.cn/egrantindex/funcindex/prjsearch-list'
driver=webdriver.Firefox(executable_path='D:\driver\geckodriver.exe') # firefox版本：80
# driver.maximize_window()
driver.get(url)
#资助类别选择 sel =
driver.find_elements_by_xpath("//select[@id='f_grantCode']/option")[2].click()
# # sel[1].click()
#
#年限选择   sel =
driver.find_elements_by_xpath("//select[@id='f_year']/option")[2].click()# 验证码操作
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

driver.back()
# driver.refresh()

# sel = driver.find_element_by_id("f_grantCode")
# sel.find_elements_by_css_selector("option")[3].click()
# print(sel.find_elements_by_css_selector("option")[3])
# print(driver.find_elements_by_xpath("//select[@id='f_grantCode']/option")[3])

# sel.find_element_by_css_selector("option[value='649']").click()
#
# #年限选择
# sel = driver.find_element_by_id("f_year")
# sel.find_elements_by_css_selector("option")[3].click()
# print(sel.find_elements_by_css_selector("option")[3])
# print(driver.find_elements_by_xpath("//select[@id='f_year']/option")[3])
# sel.find_element_by_css_selector("option[value='2018']").click()
#资助类别选择 sel =
driver.find_elements_by_xpath("//select[@id='f_grantCode']/option")[3].click()
# # sel[1].click()
#
#年限选择   sel =
driver.find_elements_by_xpath("//select[@id='f_year']/option")[3].click()

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

driver.back()
driver.quit()
