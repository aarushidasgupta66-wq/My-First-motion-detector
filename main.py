import cv2
vid=cv2.VideoCapture(0)
ret,frame=vid.read()
if not ret:
    print("failed to grab frame")
    exit()

prev_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#changes frame to grey scale
prev_gray=cv2.GaussianBlur(prev_gray,(21,21),0) #blurs out frame, 21, 21 show the blur height/width

while True:
    ret,frame=vid.read()
    if not ret:
        break

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    frame_delta= cv2.absdiff(prev_gray,gray)
    thresh = cv2.threshold(frame_delta,15,255,cv2.THRESH_BINARY)[1]
    changed_pix=cv2.countNonZero(thresh)

    if changed_pix>1000:
        print("MOTION DETECTED")
    cv2.imshow("Live cam 0",frame)
    prev_gray=gray

    if cv2.waitKey(300) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()