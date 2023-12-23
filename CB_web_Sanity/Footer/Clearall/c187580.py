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
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession > div > div.initSession_top > div.initSession_control._padHidden > div.initSession_control-block._search > div > input').send_keys("background")
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession > div > div.initSession_top > div.initSession_control._padHidden > div.initSession_control-block._search > div > input').send_keys(Keys.ENTER)
time.sleep(3)
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession_content > ul > li > div > a.buttonSessionLink > div').click()
time.sleep(4)

# 點擊"Sticker" icon
driver1.find_element(By.CSS_SELECTOR,'#floatingBoard-sticker').click()  
time.sleep(1)

# 點"圓"
driver1.find_element(By.CSS_SELECTOR,'#root > div:nth-child(5) > div > div.sticker-menu > div > section > div.sticker_contentInner.active > ul > li:nth-child(1) > a').click()          
time.sleep(1)  

# 劃一個"圓"
startx1=size['width']*0.5
starty1=size['height']*0.7
endx2=size['width']*0.8
endy2=size['height']*0.9
pyautogui.moveTo(startx1, starty1)
pyautogui.dragTo(endx2, endy2, 1, button='left')
time.sleep(1)

# 點擊Setting>Import>Files
driver1.find_element(By.CSS_SELECTOR,'#root > div.header_wrap > header > div > ul > li:nth-child(2) > a').click()
time.sleep(1)
driver1.find_element(By.CSS_SELECTOR,'#root > div.header_wrap > header > div.header_session > ul > li:nth-child(2) > div > ul > li:nth-child(3)').click()
time.sleep(1)
driver1.find_element(By.CSS_SELECTOR,'#root > div.header_wrap > header > div.header_session > ul > li:nth-child(2) > div > ul > li:nth-child(3) > div > ul > li:nth-child(1) > div').click()
time.sleep(2)

# 匯入png圖片
pyautogui.hotkey('ctrl','space')
pyautogui.write('C:\\Users\\yuki.lin\\CB_web_Sanity\\Flowting_board\\Import_file\\photos\\shiba.jpg')
pyautogui.press('Enter')
time.sleep(10)


# 選擇Pen
driver1.find_element(By.CSS_SELECTOR,'#floatingBoard-pencil').click()

# -
startx1=size['width']*0.1
starty1=size['height']*1.25
endx2=size['width']*0.3
endy2=size['height']*1.35
pyautogui.moveTo(startx1, starty1)
pyautogui.dragTo(endx2, endy2, 1, button='left')
time.sleep(1)

# 點擊下方的"clear" icon
driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_owned.footerTool_wrap > ul > li:nth-child(2) > a').click()  
time.sleep(1) 

# 點擊下方的"undo" icon
driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_owned.footerTool_wrap > ul > li:nth-child(3) > a').click()  
time.sleep(1) 

# 快照取得畫面
x1=size['width']*0.05
y1=size['height']*0.42
x2=size['width']*0.9
y2=size['height']*0.98
file1 = screenshoot.fun1(driver1,x1, y1, x2, y2)
print("file1 = "+file1)
time.sleep(1)

# 比較圖片,回傳相似結果
file2="C:\\Users\\yuki.lin\\CB_web_Sanity\\Footer\\Clearall\\undo-compare.png"
result = check.fun2(file1,file2)
time.sleep(1)
if result == 'PASS' :
   os.remove(file1)
   time.sleep(1)

# 點擊下方的"clear" icon
driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_owned.footerTool_wrap > ul > li:nth-child(2) > a').click()  
time.sleep(1) 
driver1.quit()

if result == 'PASS':
   print("PASS")
else:
   print("FAIL")
