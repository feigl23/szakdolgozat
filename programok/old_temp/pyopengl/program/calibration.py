from os import path
import glob
import sys

import cv2
import cv2.aruco as aruco
import numpy as np

class Calibration:

    def __init__(self):
        self.rvecs = None
        self.tvecs =  None
        self.mtx = None
        self.dist = None
        self.ids = None

    def calibrate(self, dirpath, prefix, image_format, square_size, width=9, height=6):
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        objp = np.zeros((height*width, 3), np.float32)
        objp[:, :2] = np.mgrid[0:width, 0:height].T.reshape(-1, 2)

        objp = objp * square_size

        objpoints = []
        imgpoints = []

        if dirpath[-1:] == '/':
            dirpath = dirpath[:-1]

        images = glob.glob(dirpath + '/' + prefix + '*.' + image_format)

        for fname in images:

            img = cv2.imread(fname)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            ret, corners = cv2.findChessboardCorners(gray, (width, height), None)

            if ret:
                objpoints.append(objp)

                corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
                imgpoints.append(corners2)

                img = cv2.drawChessboardCorners(img, (width, height), corners2, ret)

        self.ret, self.mtx, self.dist, self.rvecs, self.tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
