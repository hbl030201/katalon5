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
time.sleep(3)

# 點擊下方的"OK"
if driver1.find_elements(By.CSS_SELECTOR,'#root > div.Yaf4Bn7btJKa7QvObVKO > div > div.G9gu7acfGwtEumCxsnVG > a'):
  driver1.find_element(By.CSS_SELECTOR,'#root > div.Yaf4Bn7btJKa7QvObVKO > div > div.G9gu7acfGwtEumCxsnVG > a').click()
  time.sleep(1)

size = driver1.get_window_size()
# print("size = " + str(size))
time.sleep(1)

driver1.find_element(By.CSS_SELECTOR,'#signinEmail').send_keys("creativeboard.at03@gmail.com")
driver1.find_element(By.CSS_SELECTOR,'#signinPassword').send_keys("Ab12345678.")
time.sleep(1)
driver1.find_element(By.CSS_SELECTOR,'#SIGNIN_CB').click()
time.sleep(5)

# 點擊第一個session
                                      
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession > div > div.initSession_top > div.initSession_control._padHidden > div.initSession_control-block._search > div > input').send_keys("drawing")
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession > div > div.initSession_top > div.initSession_control._padHidden > div.initSession_control-block._search > div > input').send_keys(Keys.ENTER)
time.sleep(3)
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession_content > div.initSession_content-wrapper > ul > li > div > a.buttonSessionLink > div').click()
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

counter = 0
for i in range(1, 16, 1):
# 點擊"Sticker" icon
 driver1.find_element(By.CSS_SELECTOR,'#floatingBoard-sticker').click()  
 time.sleep(1)

# 選擇形狀
 address='#root > div:nth-child(5) > div > div.sticker-menu > div > section > div.sticker_contentInner.active > ul > li:nth-child(%s) > a' % (i)
 driver1.find_element(By.CSS_SELECTOR,address).click()          
 time.sleep(1)  

# 劃一個形狀
 startx1=size['width']*0.1
 starty1=size['height']*0.5
 endx2=size['width']*0.3
 endy2=size['height']*0.7
 pyautogui.moveTo(startx1, starty1)
 pyautogui.dragTo(endx2, endy2, 1, button='left')
 time.sleep(1)

# 選擇形狀
 startx1=size['width']*0.1
 starty1=size['height']*0.5
 endx2=size['width']*0.3
 endy2=size['height']*0.7
 pyautogui.moveTo(startx1, starty1)
 pyautogui.mouseDown(button='left')
 pyautogui.dragTo(endx2, endy2, 1, button='left')
 time.sleep(1)

#選擇 color
 for j in range(2,7,1):
  color='#white-board > div > div > div:nth-child(1) > div:nth-child(%s)' % (j)
  driver1.find_element(By.CSS_SELECTOR,color).click()
  time.sleep(1)

# 快照取得畫面
  x1=size['width']*0.05
  y1=size['height']*0.42
  x2=size['width']*0.7
  y2=size['height']*1.0
  file1 = screenshoot.fun1(driver1,x1, y1, x2, y2)
#   print("file1 = "+file1)
  time.sleep(1)

  # 比對圖片
  compare_image = 'shape' + str(i)  + '_' + str(j) + '_compare.png'
  file2="C:\\Users\mars.wu\\Katalon Studio\\CBWeb_1_0_jenkins\\CB_web_Sanity\\Flowting_board\\Sticker\\"+ compare_image
  result = check.fun2(file1,file2)
  time.sleep(1)
  if result == 'PASS' :
    os.remove(file1)
    time.sleep(1)
  else :
    counter = counter + 1  

# 點擊"垃圾桶" , 清空session
 driver1.find_element(By.CSS_SELECTOR,'#TOOLBAR_CLEARALL_CLICK').click()  
 time.sleep(1)  
driver1.quit()

if counter < 1:
   print("PASS")
else:
   print("FAIL")