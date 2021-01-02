# -*- coding:utf8 -*-
import cv2
import os
import time
# 保存图片的路径
video_path = r'video_watemark_70'
savedpath = r'images'
video_list = os.listdir(video_path)
 
# 保存图片的帧率间隔
count = 75*2
i = 0
j = 0
for index, video_name in enumerate(video_list):
    video_path_ = os.path.join(video_path, video_name)
    # 开始读视频
    videoCapture = cv2.VideoCapture(video_path_)
    print("正在处理第{}个视频，总共{}个视频".format(index+1, len(video_list)))
 
    while True:
        success, frame = videoCapture.read()
        i += 1
        if (i % count == 0):
            # 保存图片
            j += 1
            savedname = str(100497 + j) + '.jpg'
            cv2.imwrite(os.path.join(savedpath, savedname), frame)
            print('image of %s is saved' % (savedname))
 
        if not success:
            print('video is all read')
            break
    videoCapture.release()
    time.sleep(5)