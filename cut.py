# 顔の切り取り
import glob
import cv2

def cut_image():
                               
    images = glob.glob('./pixiv_images/1/*')
    
    cascade = cv2.CascadeClassifier('./lbpcascade_animeface.xml')
    
    for path in images:
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        print(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        face = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(24, 24))

        for x, y, w, h in face:
            img = img[y:y+h, x:x+w]

        save_path = './face/' + path.split('/')[-1]
        cv2.imwrite(save_path, img)


cut_image()
