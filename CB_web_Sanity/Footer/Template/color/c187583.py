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
# print("size = " + str(size))
time.sleep(1)

driver1.find_element(By.CSS_SELECTOR,'#signinEmail').send_keys("creativeboard.at03@gmail.com")
driver1.find_element(By.CSS_SELECTOR,'#signinPassword').send_keys("Ab12345678.")
time.sleep(1)
driver1.find_element(By.CSS_SELECTOR,'#SIGNIN_CB').click()
time.sleep(5)

#  點擊 background 的 session
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession > div > div.initSession_top > div.initSession_control._padHidden > div.initSession_control-block._search > div > input').send_keys("background")
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession > div > div.initSession_top > div.initSession_control._padHidden > div.initSession_control-block._search > div > input').send_keys(Keys.ENTER)
time.sleep(3)
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession_content > ul > li:nth-child(1) > div > a.buttonSessionLink > div').click()
time.sleep(3)

counter = 0
# 選擇背景 icon
for i in range(1, 37, 1):
 driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_owned.footerTool_wrap > ul > li:nth-child(1) > a').click()

# 選擇 color
 address='#root > div.yhHqF9AgCQumPIE4NQJK > div > section > div.colorThemeBox_contentInner.colorThemeBox_tabContent.active > ul > li:nth-child(%s) > a' % (i)
 driver1.find_element(By.CSS_SELECTOR,'#root > div.yhHqF9AgCQumPIE4NQJK > div > ul > li:nth-child(1) > a').click()
 driver1.find_element(By.CSS_SELECTOR,address).click()
 time.sleep(2)

#  再點擊一次背景收回
 driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_owned.footerTool_wrap > ul > li:nth-child(1) > a').click()
 time.sleep(2)

# 快照取得畫面
 x1=size['width']*0.05
 y1=size['height']*0.42
 x2=size['width']*0.9
 y2=size['height']*0.98
 file1 = screenshoot.fun1(driver1,x1, y1, x2, y2)
#  print("file1 = "+file1)
 time.sleep(2)

#   比對圖片
 compare_image = 'color' + str(i)  + '_compare.png'
 file2="C:\\Users\\yuki.lin\\CB_web_Sanity\\Footer\\Template\\color\\"+ compare_image
 result = check.fun2(file1,file2)
 time.sleep(1)
 if result == 'PASS' :
   os.remove(file1)
   time.sleep(1)
 else :
   counter = counter + 1  


# 讓背景色變回白色
driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_owned.footerTool_wrap > ul > li:nth-child(1) > a').click()
driver1.find_element(By.CSS_SELECTOR,'#root > div.yhHqF9AgCQumPIE4NQJK > div > ul > li:nth-child(1) > a > span').click()
driver1.find_element(By.CSS_SELECTOR,'#root > div.yhHqF9AgCQumPIE4NQJK > div > section > div.colorThemeBox_contentInner.colorThemeBox_tabContent.active > ul > li:nth-child(1) > a').click()
time.sleep(2)
driver1.quit()

if counter < 3:
   print("PASS")
else:
   print("FAIL")
