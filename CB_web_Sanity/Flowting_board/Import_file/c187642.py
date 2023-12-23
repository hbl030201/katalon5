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

#  點擊第一個session
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession > div > div.initSession_top > div.initSession_control._padHidden > div.initSession_control-block._search > div > input').send_keys("drawing")
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession > div > div.initSession_top > div.initSession_control._padHidden > div.initSession_control-block._search > div > input').send_keys(Keys.ENTER)
time.sleep(3)
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession_content > ul > li:nth-child(1) > div > a.buttonSessionLink > div').click()
time.sleep(3)

# 點擊Setting>Import>Files
driver1.find_element(By.CSS_SELECTOR,'#root > div.header_wrap > header > div > ul > li:nth-child(2) > a').click()
time.sleep(1)
driver1.find_element(By.CSS_SELECTOR,'#root > div.header_wrap > header > div.header_session > ul > li:nth-child(2) > div > ul > li:nth-child(3) > a').click()
time.sleep(1)
driver1.find_element(By.CSS_SELECTOR,'#root > div.header_wrap > header > div.header_session > ul > li:nth-child(2) > div > ul > li:nth-child(3) > div > ul > li:nth-child(1) > div > label').click()
time.sleep(2)

# 匯入png圖片
pyautogui.hotkey('ctrl','space')
pyautogui.write('C:\\Users\\yuki.lin\\CB_web_Sanity\\Flowting_board\\Import_file\\photos\\ghost jack olantern.png')
pyautogui.press('Enter')
time.sleep(10)

# 快照取得畫面
x1=size['width']*0.01
y1=size['height']*0.3
x2=size['width']*0.9
y2=size['height']*0.98
file1 = screenshoot.fun1(driver1,x1, y1, x2, y2)
print("file1 = "+file1)
time.sleep(1)

# 比較圖片,回傳相似結果
file2="C:\\Users\\yuki.lin\\CB_web_Sanity\\Flowting_board\\Import_file\\import-file_png-compare.png"
result = check.fun2(file1,file2)
if result == 'PASS' :
   os.remove(file1)
   time.sleep(1)

# 點擊"垃圾桶" , 清空session
driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_owned.footerTool_wrap > ul > li:nth-child(2) > a').click()  
time.sleep(1)  
driver1.quit()

if result == 'PASS':
    print("PASS")
else:
    print("FAIL")
