import numpy as np
import cv2

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.frame = None

    def get_frame(self):
        self.frame = self.cap.read()[1]
        return self.frame

