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
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession > div > div.initSession_top > div.initSession_control._padHidden > div.initSession_control-block._search > div > input').send_keys("drawing")
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession > div > div.initSession_top > div.initSession_control._padHidden > div.initSession_control-block._search > div > input').send_keys(Keys.ENTER)
time.sleep(3)
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession_content > ul > li:nth-child(1) > div > a.buttonSessionLink > div').click()
time.sleep(6)

# 將FB往上方移一點 (由於這裡時常會無法把FB拖移到上方 , 因此用迴圈 , 移動完FB後比對圖片 , 若不對再移動)
for i in range(1,4,1):
 startx1=size['width']*0.75
 starty1=size['height']*1.1
 endx2=size['width']*0.75
 endy2=size['height']*0.7
 pyautogui.moveTo(startx1, starty1)
 pyautogui.mouseDown(button='left')
 pyautogui.dragTo(endx2, endy2, 1, button='left')
 time.sleep(1)

 # 快照取得畫面
 x1=size['width']*0.05
 y1=size['height']*0.42
 x2=size['width']*0.9
 y2=size['height']*0.98
 file1 = screenshoot.fun1(driver1,x1, y1, x2, y2)
 time.sleep(1)

 # 比較圖片,回傳相似結果
 fb = "C:\\Users\\yuki.lin\\CB_web_Sanity\\Flowting_board\\Marker\\color-theme_15x3\\fb.png"
 fb_result = check.fun2(file1,fb)
 time.sleep(1)

 # 如果比對結果正確 , 則跳脫迴圈 , 不然就繼續再移動FB
 if fb_result == 'PASS' :
    os.remove(file1)
    time.sleep(1)    
    break
time.sleep(1)

counter = 0
 # 選擇Pen
driver1.find_element(By.CSS_SELECTOR,'#floatingBoard-pen').click()
for j in range(1,4,1):

 driver1.find_element(By.CSS_SELECTOR,'#root > div:nth-child(5) > div > div.floatingBoard._floatingTool.adder > div > div.floatingBoard-2st-wrap > ul > li.floatingBoard-2st-li._colorCycle._cycle1 > a').click()
 
 address1 = '#root > div:nth-child(5) > div > div.palette > div > section > div.colorThemeCycle_contentInner._theme.active > ul > li:nth-child(%s)'% (j)
 driver1.find_element(By.CSS_SELECTOR,address1).click()
 for i in range(2,9,1):
  # 點擊"color"
  address2 = '#root > div:nth-child(5) > div > div.floatingBoard._floatingTool.adder > div > div.floatingBoard-2st-wrap > ul > li.floatingBoard-2st-li._colorCycle._cycle%s > a'% (i)

  # 點擊第i種顏色
  driver1.find_element(By.CSS_SELECTOR,address2).click()                              
 
  # -
  startx1=size['width']*0.1
  starty1=size['height']*0.5
  endx2=size['width']*0.3
  endy2=size['height']*0.7
  pyautogui.moveTo(startx1, starty1)
  pyautogui.dragTo(endx2, endy2, 1, button='left')
  time.sleep(1)

  # 快照取得畫面
  x1=size['width']*0.05
  y1=size['height']*0.4
  x2=size['width']*0.9
  y2=size['height']*0.98
  file1 = screenshoot.fun1(driver1,x1, y1, x2, y2)
  print("file1 = "+file1)
  time.sleep(1)

  # 比較圖片,回傳相似結果
  compare_image = 'theme' + str(j) + '_color' + str(i) + '_compare.png'
  file2="C:\\Users\\yuki.lin\\CB_web_Sanity\\Flowting_board\\Marker\\color-theme_15x3\\"+ compare_image
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

if counter < 2:
   print("PASS")
else:
   print("FAIL")
  
