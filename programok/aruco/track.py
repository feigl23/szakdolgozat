import cv2.aruco as aruco
import numpy as np
import cv2


def find_aruco(self, frame, mtx, dist):
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_100)
    parameters = aruco.DetectorParameters_create()
    parameters.adaptiveThreshConstant = 10
    corners, ids, rejectedImgPoints = aruco.detectMarkers(image, aruco_dict,
                                                        parameters=parameters,
                                                        cameraMatrix=mtx,
                                                        distCoeff=dist)

    if np.all(self.ids is not None):
        for i in range(0, len(self.ids)):
            aruco.drawDetectedMarkers(frame, corners)
            self.run = True
            self.rvec, self.tvec ,_ = aruco.estimatePoseSingleMarkers(corners, 0.017, mtx, dist)

        return rvec, tvec, ids
    else:
        return 0,0,0
