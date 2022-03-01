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

