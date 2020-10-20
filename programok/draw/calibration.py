from os import path
import argparse
import glob
import os.path
import sys

import cv2
import cv2.aruco as aruco
import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import time

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

cap = cv2.VideoCapture(0)
global frame

def glut():
    glutInitWindowPosition(0, 0);
    glutInitWindowSize(700,700);
    glutInit(sys.argv)

    glutSetOption(GLUT_ACTION_ON_WINDOW_CLOSE, GLUT_ACTION_GLUTMAINLOOP_RETURNS);
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutCreateWindow(b"Display")


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
    #print(ret, mtx, dist)
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

def compositeArray(rvec, tvec):
    v = np.c_[rvec, tvec.T]
    #print(v)
    v_ = np.r_[v, np.array([[0,0,0,1]])]
    return v_

def track(matrix_coefficients, distortion_coefficients):
    alpha = mtx[0][0]
    beta = mtx[1][1]
    cx = mtx[0][2]
    cy = mtx[1][2]
    while True:

        ret, frame = cap.read()
        cap.set(cv2.CAP_PROP_FPS, 30)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
        #cv2.imshow('frame',image)

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
                #print(rvec,tvec)
                #aruco.drawAxis(frame, matrix_coefficients, distortion_coefficients, rvec, tvec, 0.01)
                img= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) #BGR-->RGB
                h, w = img.shape[:2]
                glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, w, h, 0, GL_RGB, GL_UNSIGNED_BYTE, img)

                ## Enable / Disable
                glDisable(GL_DEPTH_TEST)    # Disable GL_DEPTH_TEST
                glDisable(GL_LIGHTING)      # Disable Light
                glDisable(GL_LIGHT0)        # Disable Light
                glEnable(GL_TEXTURE_2D)     # Enable texture map

                ## init
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear Buffer
                glColor3f(1.0, 1.0, 1.0)    # Set texture Color(RGB: 0.0 ~ 1.0)
                glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
                glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

                ## draw background
                glMatrixMode(GL_PROJECTION)
                glLoadIdentity()
                glPushMatrix()
                glBegin(GL_QUADS)
                glTexCoord2d(0.0, 1.0)
                glVertex3d(-1.0, -1.0,  0)
                glTexCoord2d(1.0, 1.0)
                glVertex3d( 1.0, -1.0,  0)
                glTexCoord2d(1.0, 0.0)
                glVertex3d( 1.0,  1.0,  0)
                glTexCoord2d(0.0, 0.0)
                glVertex3d(-1.0,  1.0,  0)
                glEnd()
                glPopMatrix()

                ## Enable / Disable
                glEnable(GL_DEPTH_TEST)     # Enable GL_DEPTH_TEST
                glEnable(GL_LIGHTING)       # Enable Light
                glEnable(GL_LIGHT0)         # Enable Light
                glDisable(GL_TEXTURE_2D)    # Disable texture map

                ## make projection matrix
                f = 1000.0  #far
                n = 1.0     #near

                m1 = np.array([
                [(alpha)/cx, 0,       0,            0               ],
                [0,          beta/cy, 0,            0               ],
                [0,          0,       -(f+n)/(f-n), (-2.0*f*n)/(f-n)],
                [0,          0,       -1,           0               ],])
                glLoadTransposeMatrixd(m1.T)


                ## draw cube
                glMatrixMode(GL_MODELVIEW)
                glLoadIdentity()
                glPushMatrix()  #projection Push(?)

                glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [0.0,0.0,1.0,1.0])
                tvec[0][0][0] = tvec[0][0][0]
                tvec[0][0][1] = -tvec[0][0][1]
                tvec[0][0][2] = -tvec[0][0][2]

                rvec[0][0][1] = -rvec[0][0][1]
                rvec[0][0][2] = -rvec[0][0][2]
                m = compositeArray(cv2.Rodrigues(rvec)[0], tvec[0][0])
                glPushMatrix()
                glLoadTransposeMatrixd(m.T)


                glTranslatef(0, 0, -0.5)
                glutSolidCube(1.0)
                glPopMatrix()

                glPopMatrix()   #projection POP(?)


                glFlush();
                glutSwapBuffers()
                #cv2.imshow('frame',img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
if path.exists('log.txt'):
    mtx, dist = load_coefficients("log.txt")
    glut()
    track(mtx, dist)
