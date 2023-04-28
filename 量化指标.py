import cv2
import math
import numpy as np

img_l=cv2.imread('/Users/gongly/Desktop/t_data/l_data/1.jpg')
# print('img_l：',img_l.shape)

img_t=cv2.imread('/Users/gongly/Desktop/t_data/c_data/1.jpg')
# print('img_t:',img_t.shape)

h,w=img_t.shape[:2]
img=cv2.resize(img_l,(w,h))
# print('img:',img.shape)

def PSNR(img1,img2):
    mse=np.mean((img1-img2)**2)
    if mse==0:
        return 100
    PIXEL_MAX=255.0
    return 20*math.log10(PIXEL_MAX/math.sqrt(mse))

r=PSNR(img,img_t)
print('PSNR:',r)
