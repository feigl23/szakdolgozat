import cv2.aruco as aruco
import numpy as np
from calibration import *


class Track:
    def __init__(self):
        self.calibration = Calibration()
        self.rvec = None
        self.tvec = None
        self.ids = None
        self.run = False


    def find_aruco(self, frame):
        self.calibration.calibrate("images","image","png",0.015,6,9)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_100)
        parameters = aruco.DetectorParameters_create()
        parameters.adaptiveThreshConstant = 10
        corners, self.ids, rejectedImgPoints = aruco.detectMarkers(image, aruco_dict,
                                                            parameters=parameters,
                                                            cameraMatrix=self.calibration.mtx,
                                                            distCoeff=self.calibration.dist)

        if np.all(self.ids is not None):
            for i in range(0, len(self.ids)):
                aruco.drawDetectedMarkers(frame, corners)
                self.run = True
                self.rvec, self.tvec ,_ = aruco.estimatePoseSingleMarkers(corners, 0.05, self.calibration.mtx, self.calibration.dist)
        else:
            self.run = False
