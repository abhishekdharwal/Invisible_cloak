import cv2
cap=cv2.VideoCapture(0) # this is web cam

while cap.isOpened():
    ret, back=cap.read() #simply read my cam
    if ret:
        cv2.imshow("image",back) # image captured by my cam back
        if cv2.waitKey(5)==ord('q'):
            #save the image
            cv2.imwrite("image.jpg",back)
            break
            
            
cap.release()            
cv2.destroyAllWindows()            
            