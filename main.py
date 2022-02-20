import cv2
import time
import numpy as np
cap = cv2.VideoCapture(0) #open webcam device number 0 or 1
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# while True:
#     # Capture frame-by-frame
#     # frame gets the next frame in the camera, ret will obtain return value from getting the camera frame
#     # boolean variable that returns true if frame is available
#     ret, frame = cap.read()
#
#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting...")
#         break
#
#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     #Displaying image in mirror
#     flipped = cv2.flip(gray, 1)
#     # Display the resulting frame
#     # frame by frame display of video
#     cv2.imshow('frame', flipped)
#     if cv2.waitKey(1) == ord('q'):
#         break
#
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()
pTime = 0 #past Time
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #to use both pillow and opencv functions for image processing
    cTime = time.time()
    fps = 1/(cTime - pTime) #fps 170
    pTime = cTime
    #draw text string on any image denoting the font type, font scale, BGR, returns an image
    cv2.putText(img, f'FPS:{int(fps)}', (20,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2)
    cv2.imshow("Test", img) #display image in the window
    cv2.waitKey(1) #wait for 1 milli second until a key is pressed on the keyboard
