from os import path
import argparse
import glob
import os.path
import sys

import cv2
import cv2.aruco as aruco
import numpy as np

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

cap = cv2.VideoCapture(0)

def calibrate(dirpath, prefix, image_format, square_size, width=9, height=6):

    objp = np.zeros((height*width, 3), np.float32)
    objp[:, :2] = np.mgrid[0:width, 0:height].T.reshape(-1, 2)

    objp = objp * square_size

    objpoints = []
    imgpoints = []

    if dirpath[-1:] == '/':
        dirpath = dirpath[:-1]

    # TODO: Use os.path.join instead!
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

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    print(ret, mtx, dist)
    return [ret, mtx, dist, rvecs, tvecs]

def save_coefficients(mtx, dist, path):

    cv_file = cv2.FileStorage(path, cv2.FILE_STORAGE_WRITE)
    cv_file.write("K", mtx)
    cv_file.write("D", dist)

    cv_file.release()

def load_coefficients(path):

    cv_file = cv2.FileStorage(path, cv2.FILE_STORAGE_READ)

    camera_matrix = cv_file.getNode("K").mat()
    dist_matrix = cv_file.getNode("D").mat()

    cv_file.release()
    return [camera_matrix, dist_matrix]

def track(matrix_coefficients, distortion_coefficients):
    while True:

        ret, frame = cap.read()

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
        cv2.imshow('frame',image)

        parameters = aruco.DetectorParameters_create()
        parameters.adaptiveThreshConstant = 10
        corners, ids, rejectedImgPoints = aruco.detectMarkers(image, aruco_dict,
                                                            parameters=parameters,
                                                            cameraMatrix=matrix_coefficients,
                                                            distCoeff=distortion_coefficients)
        if np.all(ids is not None):
            for i in range(0, len(ids)):

                aruco.drawDetectedMarkers(frame, corners)
                rvec, tvec ,_ = aruco.estimatePoseSingleMarkers(corners, 0.05, matrix_coefficients, distortion_coefficients)
                print(rvec,tvec)
                aruco.drawAxis(frame, matrix_coefficients, distortion_coefficients, rvec, tvec, 0.05)

                cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    if path.exists('log.txt'):
        mtx, dist = load_coefficients("log.txt")
        track(mtx, dist)
    else:
        ret, mtx, dist, rvecs, tvecs  = calibrate("images","image","jpg",0.015,6,9)
        save_coefficients(mtx, dist, "log.txt")
        track(mtx,dist)
