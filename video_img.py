import cv2

# path_l='/Users/gongly/Desktop/data/1.mp4'
# path_r='/Users/gongly/Desktop/data/2.mp4'

path_l='/Users/gongly/Desktop/t_data/1.mp4'
path_r='/Users/gongly/Desktop/t_data/2.mp4'

def video_img(path):
    video=cv2.VideoCapture(path)
    #获取视频总帧数
    frames=video.get(cv2.CAP_PROP_FRAME_COUNT)
    print('视频总帧数:',frames)

    #获取视频的帧率
    fps=video.get(cv2.CAP_PROP_FPS)
    print('视频的帧率:',fps)

    #获取视频的总时长
    print('视频的总时长:',frames/fps)

    still_reading,image=video.read()
    frame_count=29
    i=1
    while still_reading:
        # cv2.imwrite(f'/Users/gongly/Desktop/data/l_data/{i}.jpg',image)
        # cv2.imwrite(f'/Users/gongly/Desktop/data/r_data/{i}.jpg', image)


        # cv2.imwrite(f'/Users/gongly/Desktop/t_data/l_data/{i}.jpg',image)
        cv2.imwrite(f'/Users/gongly/Desktop/t_data/r_data/{i}.jpg', image)
        i=i+1

        still_reading,image=video.read()
        frame_count=frame_count+29

video_img(path_r)
# video_img(path_l)

