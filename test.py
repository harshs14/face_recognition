import os
import numpy as np
import cv2
# import imutils

filename = 'video.avi'
fps = 24
res = '480p'

def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

STD_DIMENSIONS =  {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}

def get_dims(cap, res='1080p'):
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width,height = STD_DIMENSIONS[res]

    change_res(cap, width, height)
    return width, height

VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    #'mp4': cv2.VideoWriter_fourcc(*'H264'),
    # 'mp4': cv2.VideoWriter_fourcc(*'XVID'),
    # 'avi': cv2.VideoWriter_fourcc('M','J','P','G'),
}

def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
      return  VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']

# fourcc = cv2.VideoWriter_fourcc('M','J','P','G')

cap = cv2.VideoCapture(0)
video_type_cv2 = get_video_type(filename)
out = cv2.VideoWriter(filename, video_type_cv2, fps, get_dims(cap, res))
# out = cv2.VideoWriter('output.avi', fourcc, 5.0, (640,480))

while(True):
    ret, frame = cap.read()

    # frame = imutils.resize(frame, width=640,height=480)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame', frame)
    # cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()