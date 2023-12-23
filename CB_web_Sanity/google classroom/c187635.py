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

#  點擊 classroom 的 session
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession > div > div.initSession_top > div.initSession_control._padHidden > div.initSession_control-block._search > div > input').send_keys("classroom")
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession > div > div.initSession_top > div.initSession_control._padHidden > div.initSession_control-block._search > div > input').send_keys(Keys.ENTER)
time.sleep(3)
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession_content > ul > li:nth-child(1) > div > a.buttonSessionLink > div').click()
time.sleep(3)

# 將FB往上方移一點
startx1=size['width']*0.75
starty1=size['height']*1.1
endx2=size['width']*0.75
endy2=size['height']*0.7
pyautogui.moveTo(startx1, starty1)
pyautogui.mouseDown(button='left')
pyautogui.dragTo(endx2, endy2, 1, button='left')
time.sleep(1)

#import video
# 點擊 classroom>test1>video
driver1.find_element(By.CSS_SELECTOR,'#root > div.header_wrap > header > ul > li:nth-child(2)').click()
time.sleep(1)
driver1.find_element(By.CSS_SELECTOR,'#root > div.header_wrap > header > ul > div.modal-mask._popup.active > div > div.TS-content > div > div.googlePop_content-ul.classroom_select > div > div > a').click()
time.sleep(1)
WebDriverWait(driver1, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div.header_wrap > header > ul > div.modal-mask._popup.active > div > div.TS-content > div > div.googlePop_content-ul.classroom_select > div > div > ul > li:nth-child(3)'))).click()
time.sleep(2)
driver1.find_element(By.CSS_SELECTOR,'#root > div.header_wrap > header > ul > div.modal-mask._popup.active > div > div.TS-content > div > div.swal2-actions.TS-actions > button.swal2-confirm.TS-confirm.invite_pop-EmailInviteBtn.swal2-styled').click()
time.sleep(1)
WebDriverWait(driver1, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div.header_wrap > header > ul > div.attendees.classroom.popNoClose._noClose.active > section > div > div > ul:nth-child(5) > li:nth-child(2) > div > a'))).click()
time.sleep(2)

# 匯入
WebDriverWait(driver1, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div.header_wrap > header > ul > div.attendees.classroom.popNoClose._noClose.active > section > div > ul:nth-child(3) > li > a'))).click()
time.sleep(5)

# 快照取得畫面
x1=size['width']*0.01
y1=size['height']*0.3
x2=size['width']*1.4
y2=size['height']*1.2
file1 = screenshoot.fun1(driver1,x1, y1, x2, y2)
print("file1 = "+file1)
time.sleep(1)

#  比對圖片
file2="C:\\Users\\yuki.lin\\CB_web_Sanity\\google classroom\\import video_compare.png"
result = check.fun2(file1,file2)
print(result)
if result =="FAIL":
  fileC=screenshoot.fun1(driver1,x1,y1,x2,y2)
time.sleep(1)
   
 # 刪除檔案
if os.path.exists(file1):
   os.remove(file1)
else:
   print("Can not delete the file as it doesn't exists")
time.sleep(1)

# 點擊"垃圾桶" , 清空session
driver1.find_element(By.CSS_SELECTOR,'#root > div.header_wrap > header > ul > div.attendees.classroom.popNoClose._noClose.active > section > div > h3 > a').click()
time.sleep(1)
driver1.find_element(By.CSS_SELECTOR,'#root > div.header_wrap > header > ul > div.attendees.classroom.popNoClose._noClose.active > section > div > h3 > a.iconBtn-icOnly._change.googleClass_changeBtn').click()
time.sleep(1)
driver1.find_element(By.CSS_SELECTOR,'body > div.swal2-container.swal2-center.TS.swal2-backdrop-show > div > div.swal2-actions.TS-actions > button.swal2-confirm.TS-confirm.confirmBtn.justUseCheck.swal2-styled').click()
time.sleep(1)
driver1.find_element(By.CSS_SELECTOR,'#root > div.header_wrap > header > ul > div.modal-mask._popup.active > div > div.TS-content > div > div.swal2-actions.TS-actions > button.swal2-cancel.TS-cancel.swal2-styled').click()
time.sleep(1)
driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_owned.footerTool_wrap > ul > li:nth-child(2) > a').click()  
time.sleep(1)  
driver1.quit()
