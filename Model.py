import cv2

#cross-platform library developed by google
#multi modal cross platform applied ML pipelines
# A ML pipeline is a way to codify and automate the workflow it takes to produce a ML learning model
import mediapipe as mp
import time
cap = cv2.VideoCapture(0)
pTime = 0 #present time
NUM_FACE = 2 #Number of faces to detect

mpDraw = mp.solutions.drawing_utils #drawing the facial points
mpFaceMesh = mp.solutions.face_mesh #Creating the mesh of lines
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=NUM_FACE) #ML model for detecting key facial features from images, max_num_faces default 1
drawSpec = mpDraw.DrawingSpec(thickness = 1, circle_radius = 1) #controlling the thickness of lines

while True:
    #Read the frames and convert the frames in RGB
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB) #Pass the image and draw the detected landmarks on the faces

    # collection of tracked faces
    # each face represents 468 face landmarks
    # each landmark is composed of x,y,z
    # x and y are normalized to [0.0, 1.0]
    # z represents the landmark depth, center of head being the origin
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks: #looping through faces
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_CONTOURS, drawSpec, drawSpec)
            for id, lm in enumerate(faceLms.landmark): # enumerate -> iterate through a sequence but it keeps track of both the index and the element
                print(lm)
                ih, iw, ic = img.shape
                x, y = int(lm.x*iw), int(lm.y*ih)
                #The 468 facial landmarks
                cv2.putText(img, str(id), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1)
                print(id, x, y)

        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS:{int(fps)}' , (20,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Test", img)
        cv2.waitKey(1)