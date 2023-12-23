import time
import glob
from datetime import datetime
from PIL import Image, ImageChops
import os
import cv2
import matplotlib.pyplot as plt

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
 if similarity01 > 0.9990:
   return "PASS" 
 else:
   return "FAIL" 

  
