import cv2
import numpy as np
import os

#检测图像关键点
def sift_keypoints_detect(image):
    gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    sift=cv2.SIFT_create()
    keypoints,features=sift.detectAndCompute(image,None)

    keypoints_image=cv2.drawKeypoints(gray_image,keypoints,None,flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
    return keypoints_image,keypoints,features

#使用KNN检测来自左右图像的SIFT特征
def get_features_point_ensemble(features_right,features_left):
    bf=cv2.BFMatcher()
    matches=bf.knnMatch(features_right,features_left,k=2)
    matches=sorted(matches,key=lambda x:x[0].distance/x[1].distance)

    good=[]
    for m,n in matches:
        ratio=0.6
        if m.distance<ratio*n.distance:
            good.append(m)
    return good

#计算视觉变换矩阵H，用H对右图进行变换并返回全景拼接图像
def Panorama_stitching(image_right,image_left):
    _,keypoints_right,features_right=sift_keypoints_detect(image_right)
    _, keypoints_left, features_left = sift_keypoints_detect(image_left)
    goodMatch=get_features_point_ensemble(features_right,features_left)

    if len(goodMatch)>4:
        Point_coordinates_right=np.float32([keypoints_right[m.queryIdx].pt for m in goodMatch]).reshape(-1,1,2)
        Point_coordinates_left = np.float32([keypoints_left[m.trainIdx].pt for m in goodMatch]).reshape(-1, 1, 2)

        ransacReprojThreshold=4

        Homography,status=cv2.findHomography(Point_coordinates_right,Point_coordinates_left,cv2.RANSAC,ransacReprojThreshold)
        Panorama=cv2.warpPerspective(image_right,Homography,(image_right.shape[1]+image_left.shape[1],image_right.shape[0]))

        # cv2.imshow("扭曲变换后的右图",Panorama)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        Panorama[0:image_left.shape[0],0:image_left.shape[1]]=image_left

        return Panorama

if __name__=='__main__':
    #批量读取文件夹中的图片进行更改
    # l_path='/Users/gongly/Desktop/data/l_data/'
    # r_path='/Users/gongly/Desktop/data/r_data/'

    l_path = '/Users/gongly/Desktop/t_data/l_data/'
    r_path = '/Users/gongly/Desktop/t_data/r_data/'

    file_l = os.listdir(l_path)
    file_r=os.listdir(r_path)

    if len(file_l) >= len(file_r):
        file_lst = len(file_r)
    else:
        file_lst = len(file_l)

    for filename in range(1,file_lst):
    # for filename in range(1100,1200):

        img_l = cv2.imread(l_path + f'{filename}.jpg')
        img_ll=cv2.resize(img_l,(1280,1700))
        image_left=img_ll

        img_r = cv2.imread(r_path +f'{filename}.jpg')
        img_rr = cv2.resize(img_r, (1280, 1700))
        image_right = img_rr


        keypoints_image_right, keypoints_right, features_right = sift_keypoints_detect(image_right)
        keypoints_image_left, keypoints_left, features_left = sift_keypoints_detect(image_left)

        goodMatch=get_features_point_ensemble(features_right,features_left)

        all_goodmatch_image=cv2.drawMatches(image_right,keypoints_right,image_left,keypoints_left,goodMatch,None,None,None,None,flags=2)

        Panorama=Panorama_stitching(image_right,image_left)

        cv2.imwrite(f'/Users/gongly/Desktop/t_data/a_data/{filename}.jpg',Panorama)
        print(f'已完成第 {filename}.jpg 图像写入')
