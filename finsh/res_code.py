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
driver=webdriver.Firefox(executable_path='geckodriver.exe') # firefox版本：80
driver.get(url)
#资助类别选择
sel = driver.find_element_by_id("f_grantCode")
sel.find_element_by_css_selector("option[value='649']").click()

#年限选择
sel = driver.find_element_by_id("f_year")
sel.find_element_by_css_selector("option[value='2019']").click()
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
f=open('data.csv','w',encoding='utf-8')
f.write('prjNo,subjectCode,ctitle,psnName,orgName,totalAmt,startEndDate\n')
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
        f.write(f'{prjNo},{subjectCode},{ctitle},{psnName},{orgName},{totalAmt},{startEndDate}\n')
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
# 申请代码下拉框
# <div class="ac_results" style="position: absolute; width: 176px; top: 253.8px; left: 186.8px; display: block;">
# <ul>
# <li class="ac_even ac_over">B01.合成化学</li>
# <li class="ac_odd">B0101.元素化学</li><li class="ac_even">B010101.主族元素化学</li>
# <li class="ac_odd">B010102.过渡金属元素化学</li>
# <li class="ac_even">B010103.稀土与锕系元素化学</li><li class="ac_odd">B0102.无机合成</li><li class="ac_even">B010201.无机固相合成</li><li class="ac_odd">B010202.无机溶液合成</li><li class="ac_even">B010203.非常规条件下无机合成</li><li class="ac_odd">B010204.晶体生长化学</li><li class="ac_even">B010205.纳米与团簇化学</li><li class="ac_odd">B010206.功能无机分子的设计与合成</li><li class="ac_even">B0103.有机合成</li><li class="ac_odd">B010301.新试剂与新反应</li><li class="ac_even">B010302.活性中间体化学</li><li class="ac_odd">B010303.金属催化合成反应</li><li class="ac_even">B010304.有机小分子催化</li><li class="ac_odd">B010305.不对称合成</li><li class="ac_even">B010306.天然产物全合成</li><li class="ac_odd">B010307.功能有机分子的设计与合成</li><li class="ac_even">B0104.高分子合成</li><li class="ac_odd">B010401.聚合反应与方法</li><li class="ac_even">B010402.离子聚合与配位聚合</li><li class="ac_odd">B010403.自由基聚合</li><li class="ac_even">B010404.逐步聚合</li><li class="ac_odd">B010405.高分子光化学与辐射化学</li><li class="ac_even">B010406.高分子精密合成</li><li class="ac_odd">B0105.配位合成化学</li><li class="ac_even">B010501.配位反应</li><li class="ac_odd">B010502.溶液配位化学</li><li class="ac_even">B010503.功能配合物化学</li><li class="ac_odd">B010504.金属有机化学</li><li class="ac_even">B010505.配位聚合物</li><li class="ac_odd">B0106.超分子化学与组装</li><li class="ac_even">B010601.组装基元</li><li class="ac_odd">B010602.非共价相互作用与组装方法</li><li class="ac_even">B010603.动态共价键化学</li><li class="ac_odd">B010604.组装过程的动态调控</li><li class="ac_even">B010605.超分子复合物与聚合物</li><li class="ac_odd">B010606.生命功能体系的组装</li><li class="ac_even">B0107.绿色合成</li><li class="ac_odd">B010701.生物催化与生物转化</li><li class="ac_even">B010702.模拟酶与仿生合成</li><li class="ac_odd">B010703.光化学合成</li><li class="ac_even">B010704.原子与步骤经济性反应</li><li class="ac_odd">B010705.可再生资源化学</li><li class="ac_even">B010706.温和条件下的化学转化</li>
# </ul>
# </div>

#all > div.ac_results