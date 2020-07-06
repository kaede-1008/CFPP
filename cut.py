# 顔の切り取り
import glob
import cv2
import matplotlib.pyplot as plt

def cut_image():

    # path ='./face/1/33110502_p01.png'
    # image = cv2.imread(path)

    # cv2.imshow('image', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    images = glob.glob('./pixiv_images/1/*')
    
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
                    
                save_path = './face/' + file_name[0] + str(num) + '.' + file_name[1]
                cv2.imwrite(save_path, face_img)


cut_image()
