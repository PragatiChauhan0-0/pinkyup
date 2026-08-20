
import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector
from hand import send_finger_count, close_connection

hand_detector = HandDetector(maxHands=1,detectionCon=0.9,minTrackCon=0.9)

#open the default camera
cam = cv2.VideoCapture(0) # parameter = source, 0 - default camera, 1 - 2nd camera , 2 - 3rd camera

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

try:

    while True:

        ret, frame = cam.read()

        if ret == False:
            break

        hands,image  = hand_detector.findHands(frame, flipType=True) 

        if hands:

            fingers = hand_detector.fingersUp(hands[0])
            send_finger_count(fingers)  # Send the finger count to Arduino
            
        cv2.imshow("Image",image)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) == ord('q'):
            break

except Exception as e:
    print("ERROR:", e, flush=True)
    input("Press Enter to exit...")

# Release the capture and writer objects
cam.release()
close_connection()  # Close the serial connection

cv2.destroyAllWindows()

# fingers detection [5 fingers]