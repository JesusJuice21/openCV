import os
import cv2

# path='/Users/gongly/Desktop/data/adata/'
path='/Users/gongly/Desktop/t_data/a_data/'

filelist=os.listdir(path)
index=len(filelist)
# print('index:',index)

for i in range(1,index):
    img=cv2.imread(path+f'{i}.jpg')
    # cv2.imwrite(f'/Users/gongly/Desktop/data/cdata/{i}.jpg',img[0:1700,0:1500])
    cv2.imwrite(f'/Users/gongly/Desktop/t_data/c_data/{i}.jpg', img[0:1700, 0:1500])
    print(f"第 {i} 张图片已写入")
