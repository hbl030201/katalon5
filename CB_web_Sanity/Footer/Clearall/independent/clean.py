import time
import pyautogui
import os
from screen import screenshoot
from CheckImage import check
from time import sleep
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
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

driver1.find_element(By.CSS_SELECTOR,'#signinEmail').send_keys("optoma108@gmail.com")
driver1.find_element(By.CSS_SELECTOR,'#signinPassword').send_keys("Ab12345678.")
time.sleep(1)
driver1.find_element(By.ID,"signSubmit").click()
time.sleep(2)

#  點擊第一個session
driver1.find_element(By.CSS_SELECTOR,'#root > div.content > div.initSession_content > ul > li > div > a.buttonSessionLink > div').click()
time.sleep(4)


# 選擇Pen
driver1.find_element(By.CSS_SELECTOR,'#floatingBoard-pencil').click()

# 畫"-"
startx1=size['width']*0.1
starty1=size['height']*0.5
endx2=size['width']*0.3
endy2=size['height']*0.7
pyautogui.moveTo(startx1, starty1)
pyautogui.dragTo(endx2, endy2, 1, button='left')
time.sleep(1)

# 選擇背景 icon
driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_owned.footerTool_wrap > ul > li:nth-child(1) > a').click()

# 選擇 color
driver1.find_element(By.CSS_SELECTOR,'#root > div.yhHqF9AgCQumPIE4NQJK > div > ul > li:nth-child(1) > a > span').click()
driver1.find_element(By.CSS_SELECTOR,'#root > div.yhHqF9AgCQumPIE4NQJK > div > section > div.colorThemeBox_contentInner.colorThemeBox_tabContent.active > ul > li:nth-child(5) > a').click()
time.sleep(2)

#  再點擊一次背景收回
driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_owned.footerTool_wrap > ul > li:nth-child(1) > a').click()
time.sleep(2)

# 點擊"向右加一頁"
driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_viewer.footerTool_wrap > ul > li:nth-child(2) > a').click()
time.sleep(2)
driver1.find_element(By.CSS_SELECTOR,'#list > li > ul > li:nth-child(3) > a').click()
time.sleep(3)

# 再點一次Page roll收合(這一步是避免沒收合直接點FB上的icon需要點2次才有反應)
driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_viewer.footerTool_wrap > ul > li:nth-child(2) > a').click()
time.sleep(2)

# 選擇背景 icon
driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_owned.footerTool_wrap > ul > li:nth-child(1) > a').click()

# 選擇 color
driver1.find_element(By.CSS_SELECTOR,'#root > div.yhHqF9AgCQumPIE4NQJK > div > ul > li:nth-child(1) > a > span').click()
driver1.find_element(By.CSS_SELECTOR,'#root > div.yhHqF9AgCQumPIE4NQJK > div > section > div.colorThemeBox_contentInner.colorThemeBox_tabContent.active > ul > li:nth-child(7) > a').click()
time.sleep(2)

#  再點擊一次背景收回
driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_owned.footerTool_wrap > ul > li:nth-child(1) > a').click()
time.sleep(2)

# 點擊"marker" icon
driver1.find_element(By.CSS_SELECTOR,'#floatingBoard-pen').click()     

# -
startx1=size['width']*0.2
starty1=size['height']*0.5
endx2=size['width']*0.4
endy2=size['height']*0.7
pyautogui.moveTo(startx1, starty1)
pyautogui.dragTo(endx2, endy2, 1, button='left')
time.sleep(1)

# 點擊下方的"clear" icon
driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_owned.footerTool_wrap > ul > li:nth-child(2) > a').click()  
time.sleep(1) 

#開啟 page roll
driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_viewer.footerTool_wrap > ul > li:nth-child(2) > a').click()
time.sleep(2)

# 快照取得畫面
x1=size['width']*0.05
y1=size['height']*0.4
x2=size['width']*0.9
y2=size['height']*0.98
file1 = screenshoot.fun1(driver1,x1, y1, x2, y2)
print("file1 = "+file1)
time.sleep(1)

# 比較圖片,回傳相似結果
file2="C:\\Users\\yuki.lin\\CB_web_Single\\Footer\\Clearall\\independent\\clean-compare.png"
result = check.fun2(file1,file2)
# print("result = "+result)
print(result)
time.sleep(1)

# 刪除 page    
driver1.find_element(By.CSS_SELECTOR,'#list > li.pageRoll_li.active > ul > li:nth-child(2) > a').click()
time.sleep(2)  
driver1.find_element(By.CSS_SELECTOR,'body > div.swal2-container.swal2-center.TS.swal2-backdrop-show > div > div.swal2-actions.TS-actions > button.swal2-confirm.TS-confirm.confirmBtn.justUseCheck.swal2-styled').click() 
time.sleep(2)

# 還原
driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_owned.footerTool_wrap > ul > li:nth-child(2) > a').click()  
time.sleep(1) 
driver1.find_element(By.CSS_SELECTOR,'#root > div.footerTool > section.footerTool_owned.footerTool_wrap > ul > li:nth-child(1) > a').click()
driver1.find_element(By.CSS_SELECTOR,'#root > div.yhHqF9AgCQumPIE4NQJK > div > section > div.colorThemeBox_contentInner.colorThemeBox_tabContent.active > ul > li:nth-child(1) > a').click()
time.sleep(2)
driver1.quit()

# 刪除檔案
if os.path.exists(file1):
    os.remove(file1)
else:
    print("Can not delete the file as it doesn't exists")
