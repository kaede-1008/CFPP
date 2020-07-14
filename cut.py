# 顔の切り取り
import glob
import cv2
import matplotlib.pyplot as plt
import os

def cut_image():
    
    auther_num = 7
    for i in range(7):
        pic_num = 0
        auther_folder = './face/' + str(i) + '/'
        folder_path = './pixiv_images/' + str(i) + '/*'
        if not os.path.exists(auther_folder):
            os.mkdir(auther_folder)
        images = glob.glob(folder_path)
        
        cascade = cv2.CascadeClassifier('./lbpcascade_animeface.xml')


        for path in images:
            img = cv2.imread(path, cv2.IMREAD_COLOR)
            # print(img)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = cv2.equalizeHist(gray)

            face = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(24, 24))
            # print(len(face))
            file_name = path.split('/')[-1].split('.')

            

            if len(face) > 0:
                for num in range(len(face)):
                    x = face[num][0]
                    y = face[num][1]
                    w = face[num][2]
                    h = face[num][3]
                    face_img = img[y:y+h, x:x+w]
                    save_path = './face/' + str(i) + '/' + str(pic_num) + '.' + file_name[1]
                    cv2.imwrite(save_path, face_img)
                    pic_num += 1

cut_image()
