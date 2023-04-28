import numpy as np
import os
import cv2


size=(1700,1500)
#图片路径
# path = '/Users/gongly/Desktop/data/cdata/'
path='/Users/gongly/Desktop/t_data/c_data/'
#保存路径
# sav_path='/Users/gongly/Desktop/data/t1.mp4'
sav_path='/Users/gongly/Desktop/t_data/t1.mp4'

all_files=os.listdir(path)
index=len(all_files)
# print(len(all_files))

fourcc=cv2.VideoWriter_fourcc(*'mp4v')
videowriter=cv2.VideoWriter(sav_path,fourcc,29,size)

img_array=[]

for filename in [path+r'{0}.jpg'.format(i) for i in range(1,index)]:
    img=cv2.imread(filename)
    if img is None:
        print(filename+'is error!')
        continue
    img_array.append(img)

print('index:',index)
print('img_array:',len(img_array))

#合成视频
for i in range(1,index-1):
    img_array[i]=cv2.resize(img_array[i],size)
    videowriter.write(img_array[i])
    print('第{}张图片合成成功！'.format(i))

print('-----done-----')
