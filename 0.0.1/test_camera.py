import picamera
import picamera.array
import time
import cv2

with picamera.Picamera as cam:
	rawCap=picamera.array.PiRGBArray(cam)
	cam.start_preview()
	time.sleep(3)
	cam.capture(rawCap,format="bgr")
	image=rawCap.array
cv2.imshow("Test",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
