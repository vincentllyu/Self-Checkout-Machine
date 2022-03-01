# import the necessary packages
#from pyimagesearch import simple_barcode_detection
from imutils.video import VideoStream
import time
import cv2
import numpy as np
import imutils
from pyzbar import pyzbar
def detect(image):
    barcodes = pyzbar.decode(image)
    result = []
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        result.append(barcode.data.decode("utf-8"))
    return result

vs = VideoStream(src=0).start()
time.sleep(2.0)

    # keep looping over the frames
while True:
	# grab the current frame and then handle if the frame is returned
	# from either the 'VideoCapture' or 'VideoStream' object,
	# respectively
	frame = vs.read()
 
	# check to see if we have reached the end of the
	# video
	if frame is None:
		break
	# detect the barcode in the image
	bc = detect(frame)
	if len(bc) > 0:
		print(bc)
		time.sleep(1)
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# if the 'q' key is pressed, stop the loop  
	if key == ord("q"):
		break

vs.stop()
# close all windows
cv2.destroyAllWindows()
