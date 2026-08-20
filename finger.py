
import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector

hand_detector = HandDetector(maxHands=1,detectionCon=0.9,minTrackCon=0.9)

#open the default camera
cam = cv2.VideoCapture(0) # parameter = source, 0 - default camera, 1 - 2nd camera , 2 - 3rd camera

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))


while True:
    ret, frame = cam.read()

    # Write the frame to the output file

    lms,image  = hand_detector.findHands(frame)
    cv2.imshow("Image",image)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and writer objects
cam.release()

cv2.destroyAllWindows()

# fingers detection [5 fingers]