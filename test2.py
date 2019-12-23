import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    # frame = imutils.resize(frame, width=640,height=480)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()