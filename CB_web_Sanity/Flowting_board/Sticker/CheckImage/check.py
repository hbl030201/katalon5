import time
import glob
from datetime import datetime
from PIL import Image, ImageChops
import os
import cv2
import matplotlib.pyplot as plt

# import ImageChops
# from skimage.metrics import structural_similarity

# fun1主要是將圖片轉換成相同比例的圖片
# def fun1(file):
#   img = Image.open(file)   # 開啟圖片
#   img2 = img.resize((600,600))         # 調整圖片尺寸為 200x200
#   img2.save('def.png')     


# def fun2(file1,file2):
#  imageA = cv2.imread(file1)
#  imageB = cv2.imread(file2)

#  # 將圖片轉換成灰階
#  grayA = cv2.cvtColor(imageA,cv2.COLOR_BGR2GRAY)
#  grayB = cv2.cvtColor(imageB,cv2.COLOR_BGR2GRAY)

#  # 比較2個圖片差異性(越接近1表示越相同,100%相同就是"1.0")
#  ssim = structural_similarity(grayA,grayB)
#  print("相似度 = "+ str(ssim))
#  if ssim > 0.999:
#    return "PASS" 
#  else:
#    return "FAIL" 


# def fun2(file1,file2,tag_value):
  # img01 = cv2.imread(file1)
  # img02 = cv2.imread(file2)
  # H1 = cv2.calcHist([img01], [tag_value], None, [256], [0,256])
  # H1 = cv2.normalize(H1, H1, 0, 1, cv2.NORM_MINMAX, -1)
  # H2 = cv2.calcHist([img02], [tag_value], None, [256], [0,256])
  # H2 = cv2.normalize(H2, H2, 0, 1, cv2.NORM_MINMAX, -1)
  # similarity01 = cv2.compareHist(H1, H2, 0)
  # print(similarity01)
  # return similarity01

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
#  print(str(similarity01))
 if similarity01 > 0.99999:
   return "PASS" 
 else:
   return "FAIL" 

# def fun2(file1,file2):
#  im1 = Image.open(file1)
#  im2 = Image.open(file2)
#  diff = ImageChops.difference(im2, im1)
#  print(diff)
#  return diff

  
