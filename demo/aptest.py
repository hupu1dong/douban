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

options = webdriver.FirefoxOptions()
options.add_argument("--proxy-server=http://171.11.28.97:9999")
options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69"')
url='https://isisn.nsfc.gov.cn/egrantindex/funcindex/prjsearch-list'
driver=webdriver.Firefox(executable_path='D:\driver\geckodriver.exe',options=options) # firefox版本：80
driver.maximize_window()
driver.get(url)
driver.find_element_by_xpath("//a[@id='f_subjectCode_img']").click()
sleep(1)
nc = driver.find_elements_by_xpath("//div[@id='f_subjectCode_treeId']/li/button")
# for s in range(len(nc)):
#     print('元素：',nc[s].text)
nc[0].click()
sleep(1)
nc2 = driver.find_elements_by_xpath("//div[@id='f_subjectCode_treeId']/li//ul/li//span")
for j in range(len(nc2)):
        driver.find_elements_by_xpath("//div[@id='f_subjectCode_treeId']/li//ul/li//span")[j].click()
        sleep(1)
        driver.find_element_by_xpath("//a[@id='f_subjectCode_img']").click()
        sleep(1)
        driver.find_elements_by_xpath("//div[@id='f_subjectCode_treeId']/li/button")[0].click()
        sleep(2)
# nc = driver.find_elements_by_xpath("//div[@id='f_subjectCode_treeId']/li/button")

for i in range(1,len(nc)):
    for j in range(len(nc2)):
        driver.find_element_by_xpath("//a[@id='f_subjectCode_img']").click()
        sleep(1)
        nc = driver.find_elements_by_xpath("//div[@id='f_subjectCode_treeId']/li/button")
        nc[i].click()
        sleep(1)
        nc2 = driver.find_elements_by_xpath("//div[@id='f_subjectCode_treeId']/li//ul/li//span")
        nc2[j].click()
        sleep(2)
    nc = driver.find_elements_by_xpath("//div[@id='f_subjectCode_treeId']/li/button")
    nc2 = driver.find_elements_by_xpath("//div[@id='f_subjectCode_treeId']/li//ul/li//span")

else:
    driver.quit()