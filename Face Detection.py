from tkinter import Button
import cv2
trained_faces_data =cv2.CascadeClassifier('faces.xml')
#test face detection on my pic
# to test with pic pic = cv2.imread('img2.jpg')
# 7atit bch y5ou default webcam 
cam= cv2.VideoCapture(0)
#bch nafichiw el frames lkol
while True:
    frame_read,frame=cam.read()
      #tawa bch nrdouha grayscale
    grayscale_pic=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces
    face_coordinates = trained_faces_data.detectMultiScale(grayscale_pic,scaleFactor=1.1,minNeighbors=5)
    
    #tawa bch n7tou square ala el pic 
    #print(face_coordinates)
    for(x,y,w,h) in (face_coordinates):
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2  )
#   cv2.imshow ie7lena el window eli fiha el img
    cv2.imshow('Face Detector', frame)
    #bch kol 1 msec yt3da lel frame eli b3dha  
    key =cv2.waitKey(1)
    #button bch tsaker el prog
    if key==113 or key==81:
        break
print("Done")
