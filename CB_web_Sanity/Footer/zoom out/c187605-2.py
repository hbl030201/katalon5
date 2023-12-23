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

#  點擊 zoom 的 session
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession > div > div.initSession_top > div.initSession_control._padHidden > div.initSession_control-block._search > div > input').send_keys("zoom")
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession > div > div.initSession_top > div.initSession_control._padHidden > div.initSession_control-block._search > div > input').send_keys(Keys.ENTER)
time.sleep(3)
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession_content > ul > li:nth-child(1) > div > a.buttonSessionLink > div').click()
time.sleep(6)

# 將FB往上方移一點
startx1=size['width']*0.75
starty1=size['height']*1.1
endx2=size['width']*0.75
endy2=size['height']*0.7
pyautogui.moveTo(startx1, starty1)
pyautogui.mouseDown(button='left')
pyautogui.dragTo(endx2, endy2, 1, button='left')
time.sleep(1)

#import 圖片
# 點擊Setting>Import>Files
driver1.find_element(By.CSS_SELECTOR,'#root > div.header_wrap > header > div > ul > li:nth-child(2) > a').click()
time.sleep(1)
driver1.find_element(By.CSS_SELECTOR,'#root > div.header_wrap > header > div.header_session > ul > li:nth-child(2) > div > ul > li:nth-child(3) > a').click()
time.sleep(1)
driver1.find_element(By.CSS_SELECTOR,'#root > div.header_wrap > header > div.header_session > ul > li:nth-child(2) > div > ul > li:nth-child(3) > div > ul > li:nth-child(1) > div > label').click()
time.sleep(2)

# 匯入jpg圖片
pyautogui.hotkey('ctrl','space')
pyautogui.write('C:\\Users\\yuki.lin\\CB_web_Sanity\\Flowting_board\\Import_file\\photos\\shiba.jpg')
pyautogui.press('Enter')
time.sleep(10)

# 選擇Pen
driver1.find_element(By.CSS_SELECTOR,'#floatingBoard-pencil').click()

# 畫畫
startx1=size['width']*0.5
starty1=size['height']*0.9
endx2=size['width']*1.2
endy2=size['height']*1.2
pyautogui.moveTo(startx1, starty1)
pyautogui.dragTo(endx2, endy2, 1, button='left')
time.sleep(1)

#import sticker
# 點擊"Sticker" icon
driver1.find_element(By.CSS_SELECTOR,'#floatingBoard-sticker').click()  
time.sleep(1)

# 點"o"
driver1.find_element(By.CSS_SELECTOR,'#root > div:nth-child(5) > div > div.sticker-menu > div > section > div.sticker_contentInner.active > ul > li:nth-child(1) > a').click()          
time.sleep(1)  

# 劃一個"o"
startx1=size['width']*0.5
starty1=size['height']*0.8
endx2=size['width']*0.8
endy2=size['height']*1.0
pyautogui.moveTo(startx1, starty1)
pyautogui.dragTo(endx2, endy2, 1, button='left')
time.sleep(1)

counter = 0
# 點7次 zoom in
for i in range(1, 8, 1):
 driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_zoom.footerTool_wrap > ul > li:nth-child(3) > a').click() 
 time.sleep(1)


# 點10次 zoom out
for i in range(1, 10, 1):
 driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_zoom.footerTool_wrap > ul > li:nth-child(1) > a').click() 
 time.sleep(1) 

 # 快照取得畫面
 x1=size['width']*0.01
 y1=size['height']*0.4
 x2=size['width']*1.4
 y2=size['height']*1.0
 file1 = screenshoot.fun1(driver1,x1, y1, x2, y2)
 print("file1 = "+file1)
 time.sleep(1)

#  比對圖片
 compare_image = 'zoom' + str(i)  + '_compare.png'
 file2="C:\\Users\\yuki.lin\\CB_web_Sanity\\Footer\\zoom out\\"+ compare_image
 result = check.fun2(file1,file2)
 time.sleep(1)
 if result == 'PASS' :
   os.remove(file1)
   time.sleep(1)
 else :
   counter = counter + 1  

# 點擊"垃圾桶" , 清空session
driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_owned.footerTool_wrap > ul > li:nth-child(2) > a').click()  
time.sleep(1)  
driver1.quit()

# print("counter = " + str(counter))
time.sleep(1)
if counter < 1:
   print("PASS")
else:
   print("FAIL")
