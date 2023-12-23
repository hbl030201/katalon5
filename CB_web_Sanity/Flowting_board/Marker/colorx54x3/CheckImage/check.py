import time
import glob
from datetime import datetime
from PIL import Image, ImageChops
import os
import cv2
import matplotlib.pyplot as plt
# from skimage.metrics import structural_similarity

# def fun2(file1,file2):
#  imageA = cv2.imread(file1)
#  imageB = cv2.imread(file2)

#  # 將圖片轉換成灰階
#  grayA = cv2.cvtColor(imageA,cv2.COLOR_BGR2GRAY)
#  grayB = cv2.cvtColor(imageB,cv2.COLOR_BGR2GRAY)

#  # 比較2個圖片差異性(越接近1表示越相同,100%相同就是"1.0")
#  ssim = structural_similarity(grayA,grayB)
#  print("相似度 = "+ str(ssim))
#  if ssim > 0.998:
#    return "PASS" 
#  else:
#    return "FAIL" 

def fun2(file1,file2):  
 imageA = cv2.imread(file1)
 imageB = cv2.imread(file2)
 color = ('b','g','r')
 for i, col in enumerate(color):
  histr1 = cv2.calcHist([imageA],[i],None,[256],[0, 256])
  plt.plot(histr1, color = col)
  plt.xlim([0, 256])
 histr1 = cv2.normalize(histr1, histr1, 0, 1, cv2.NORM_MINMAX, -1)
 for i, col in enumerate(color):
  histr2 = cv2.calcHist([imageB],[i],None,[256],[0, 256])
  plt.plot(histr2, color = col)
  plt.xlim([0, 256])
 histr2 = cv2.normalize(histr2, histr2, 0, 1, cv2.NORM_MINMAX, -1)
 similarity01 = cv2.compareHist(histr1, histr2, 0)
 print(str(similarity01))
 if similarity01 > 0.99999:
   return "PASS" 
 else:
   return "FAIL"
