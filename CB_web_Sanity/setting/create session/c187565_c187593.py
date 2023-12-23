import time
import pyautogui
import os
from screen import screenshoot
from CheckImage import check
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

def is_exist(elements):
  if driver1.find_element(By.XPATH,elements):
    driver1.find_element(By.XPATH,elements).click()
  else:
    time.sleep(1)
    is_exist(elements)

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

counter = 0
# 建立 session
for i in range (1,110,1):
 address = '/html/body/div/div[2]/div[1]/div/div[2]/ul/li[%s]'%(i)
 is_exist(address)
 time.sleep(8)

 # 快照取得畫面
 x1=size['width']*0.05
 y1=size['height']*0.4
 x2=size['width']*1.3
 y2=size['height']*1.0
 file1 = screenshoot.fun1(driver1,x1, y1, x2, y2)
 time.sleep(1)

  # 比較圖片,回傳相似結果
 compare_image = 'theme' + str(i) + '_compare.png'
 file2="C:\\Users\\yuki.lin\\CB_web_Sanity\\setting\\create session\\"+ compare_image
 result = check.fun2(file1,file2)
 if result == 'PASS' :
   os.remove(file1)
   time.sleep(1)
 else :
   counter+=1
   a = str(i)
   time.sleep(1) 

  # 點擊"垃圾桶" , 清空session
 driver1.find_element(By.CSS_SELECTOR,'#root > div.header_wrap > header > div.header_session > ul > li:nth-child(2) > a').click()
 time.sleep(1) 
 driver1.find_element(By.CSS_SELECTOR,'#root > div.header_wrap > header > div.header_session > ul > li:nth-child(2) > div > ul > li:nth-child(5)').click()  
 time.sleep(1)
 driver1.find_element(By.CSS_SELECTOR,'body > div.swal2-container.swal2-center.TS.swal2-backdrop-show > div > div.swal2-actions.TS-actions > button.swal2-confirm.TS-confirm.confirmBtn.justUseCheck.swal2-styled').click()  
 time.sleep(2)
driver1.quit() 

if counter < 3:
   print("PASS")
else:
   print("FAIL")