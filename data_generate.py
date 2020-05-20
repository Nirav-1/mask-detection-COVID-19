#creating database
import cv2, os

#os.chdir("D:\\project\\face_mask_detection\\face-mask-detector")
haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'training_data'  #All the faces data will be present this folder
sub_data = 'without mask'

path = os.path.join(datasets, sub_data)
if not os.path.isdir(path):
    os.mkdir(path)
(width, height) = (310, 275)    # defining the size of images

face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0) #'0' is use for my webcam, if you've any other camera attached use '1' like this

count = 1
while count < 226:
    (_, im) = webcam.read()
    faces = face_cascade.detectMultiScale(im, 1.3, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        face = im[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
#
        cv2.imwrite('%s/%s.jpg' % (path,count), face_resize)
        print('Creating...' + '%s/%s.jpg' % (path,count))
    count += 1

    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(10)
    if key == 27:
        break

# Release all space and windows once done
webcam.release()
cv2.destroyAllWindows()