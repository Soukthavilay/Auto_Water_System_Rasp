import cv2
#https://pyimagesearch.com/2017/02/06/faster-video-file-fps-with-cv2-videocapture-and-opencv/
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)
fps = int(cap.get(5))
print("fps:", fps)

while(cap.isOpened()):
    ret,frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    if k == 27:
        break