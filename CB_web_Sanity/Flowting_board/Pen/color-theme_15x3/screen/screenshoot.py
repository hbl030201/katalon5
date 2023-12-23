from datetime import datetime
import os
import pyautogui

def fun1(a,x1, y1, x2, y2):
 result = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
 result = os.path.join(result + '.png')

 # 擷取圖片,並設定時間當成名稱
#  print("照片名稱是:" + result)
 myScreenshot = pyautogui.screenshot(region=(x1, y1, x2, y2))
 myScreenshot.save(result)
 image = str(result)
#  print("檔案位置是1:" + image)

 # 存放位置
 file ='C:\\Users\\yuki.lin\\CB_web_Sanity\\Flowting_board\\Pen\\color-theme_15x3\\' + image
#  file ='C:\\KatalonStudio\\CBWeb\\' + image
 return file
