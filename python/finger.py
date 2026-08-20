
import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector

print("PROGRAM STARTED", flush=True)
hand_detector = HandDetector(maxHands=2,detectionCon=0.9,minTrackCon=0.9)

#open the default camera
cam = cv2.VideoCapture(0) # parameter = source, 0 - default camera, 1 - 2nd camera , 2 - 3rd camera

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))


while True:
    ret, frame = cam.read()

    if ret == False:
        break

    hands,image  = hand_detector.findHands(frame, flipType=True) 

    print("Hands detected:", len(hands))

    if hands:

        for hand in hands:
            print(hand["type"])
            fingers = hand_detector.fingersUp(hand)
            
            print("Fingers:", fingers) 

    cv2.imshow("Image",image)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and writer objects
cam.release()

cv2.destroyAllWindows()

# fingers detection [5 fingers]