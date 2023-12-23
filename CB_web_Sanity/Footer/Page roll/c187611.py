import time
import pyautogui
import os
from screen import screenshoot
from CheckImage import check
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

login_email = "find_element(By.CSS_SELECTOR,'#signinEmail')"
caps = webdriver.DesiredCapabilities.CHROME.copy()
caps['acceptInsecureCerts'] = True
driver1 = webdriver.Chrome(desired_capabilities=caps)
driver1.get("https://creativeboard.optoma.com/signin")

# driver1.maximize_window()
driver1.set_window_position(x=0, y=0)
driver1.set_window_size(1250,680)
time.sleep(1)

size = driver1.get_window_size()
time.sleep(1)

driver1.find_element(By.CSS_SELECTOR,'#signinEmail').send_keys("creativeboard.at@gmail.com")
driver1.find_element(By.CSS_SELECTOR,'#signinPassword').send_keys("Ab12345678.")
time.sleep(1)
driver1.find_element(By.CSS_SELECTOR,'#SIGNIN_CB').click()
time.sleep(5)

#  點擊 delete page 的 session
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession > div > div.initSession_top > div.initSession_control._padHidden > div.initSession_control-block._search > div > input').send_keys("delete page")
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession > div > div.initSession_top > div.initSession_control._padHidden > div.initSession_control-block._search > div > input').send_keys(Keys.ENTER)
time.sleep(3)
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession_content > ul > li:nth-child(1) > div > a.buttonSessionLink > div').click()
time.sleep(3)

# 先點擊Page roll
driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_viewer.footerTool_wrap > ul > li:nth-child(2)').click()
time.sleep(2)

# 先點擊"向右加一頁"
driver1.find_element(By.CSS_SELECTOR,'#list > li > ul > li:nth-child(3) > a').click()
time.sleep(5)

# 刪除 page
driver1.find_element(By.CSS_SELECTOR,'#list > li.pageRoll_li.active > ul > li:nth-child(2) > a').click()
time.sleep(2)  
driver1.find_element(By.CSS_SELECTOR,'body > div.swal2-container.swal2-center.TS.swal2-backdrop-show > div > div.swal2-actions.TS-actions > button.swal2-confirm.TS-confirm.confirmBtn.justUseCheck.swal2-styled').click() 
time.sleep(2)

# 快照取得畫面
x1=size['width']*0.05
y1=size['height']*0.4
x2=size['width']*1.1
y2=size['height']*1.0
file1 = screenshoot.fun1(driver1,x1, y1, x2, y2)
time.sleep(1)

# 比較圖片,回傳相似結果
file2="C:\\Users\\yuki.lin\\CB_web_Sanity\\Footer\\Page roll\\delete-Page.compare.png"
result = check.fun2(file1,file2)
time.sleep(1)
if result == 'PASS' :
   os.remove(file1)
   time.sleep(1)

# # 點擊"垃圾桶" , 清空session 
driver1.quit()

if result == 'PASS' :
   print("PASS")
else:
   print("FAIL")
