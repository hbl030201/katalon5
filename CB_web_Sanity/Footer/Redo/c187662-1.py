import time
import pyautogui
import os
from screen import screenshoot
from CheckImage import check
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.action_chains import ActionChains
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

driver1.find_element(By.CSS_SELECTOR,'#signinEmail').send_keys("creativeboard.at03@gmail.com")
driver1.find_element(By.CSS_SELECTOR,'#signinPassword').send_keys("Ab12345678.")
time.sleep(1)
driver1.find_element(By.CSS_SELECTOR,'#SIGNIN_CB').click()
time.sleep(5)

#  點擊 drawing 的 session
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession > div > div.initSession_top > div.initSession_control._padHidden > div.initSession_control-block._search > div > input').send_keys("drawing")
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession > div > div.initSession_top > div.initSession_control._padHidden > div.initSession_control-block._search > div > input').send_keys(Keys.ENTER)
time.sleep(3)
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession_content > ul > li:nth-child(1) > div > a.buttonSessionLink > div').click()
time.sleep(3)

# 選擇Pen
driver1.find_element(By.CSS_SELECTOR,'#floatingBoard-pencil').click()

# 畫30筆
for i in range(300, 800, 100):
   for j in range(300, 900, 100): 
      pyautogui.moveTo(i, j) 
      pyautogui.dragTo(i+50, j+50, 1, button='left')
      time.sleep(1)

pyautogui.moveTo(800, 300) 
pyautogui.dragTo(850, 350, 1, button='left')
time.sleep(1)

# 點30次 undo
for i in range(1, 32, 1):
 driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_owned.footerTool_wrap > ul > li:nth-child(3) > a').click() 
 time.sleep(1)

counter = 0

# 再點30次redo,然後驗證,刪檔案
for i in range(1, 32, 1):
 driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_owned.footerTool_wrap > ul > li:nth-child(4) > a').click() 
 time.sleep(1)

 # 快照取得畫面
 x1=size['width']*0.01
 y1=size['height']*0.3
 x2=size['width']*1.0
 y2=size['height']*1.1
 file1 = screenshoot.fun1(driver1,x1, y1, x2, y2)
 time.sleep(1)

 # 比對圖片
 compare_image = 'redo' + str(i)  + '_compare.png'
 file2="C:\\Users\\yuki.lin\\CB_web_Sanity\\Footer\\Redo\\"+ compare_image
 result = check.fun2(file1,file2)
 if result == 'PASS' :
   os.remove(file1)
   time.sleep(1)
 else :
   counter+=1
   a = str(i)
   # print("error = " + a)
   time.sleep(1)  

# 點擊"垃圾桶" , 清空session
driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_owned.footerTool_wrap > ul > li:nth-child(2) > a').click()  
time.sleep(1)  
driver1.quit()

if counter < 1:
   print("PASS")
else:
   print("FAIL")