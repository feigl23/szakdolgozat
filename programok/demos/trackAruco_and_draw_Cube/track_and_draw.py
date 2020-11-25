# -*- coding: utf-8 -*-
##A demóhoz felhasznált kódrész: https://stackoverflow.com/questions/50764623/object-is-wrong-displaced-in-ar-aruco-opengl

import cv2
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import cv2.aruco as aruco
import numpy as np

cap = cv2.VideoCapture(0)

class Cube:
    def __init__(self):
        self.x = 500
        self.y = 150
        self.width =500
        self.height = 500
        self.mtx = None
        self.dist = None

    def load_coefficients(self,path):
        cv_file = cv2.FileStorage(path, cv2.FILE_STORAGE_READ)
        camera_matrix = cv_file.getNode("CameraMatrix").mat()
        dist_matrix = cv_file.getNode("DistortionCoeff").mat()
        cv_file.release()
        return [camera_matrix, dist_matrix]

    def find_aruco(self, frame):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_100)
        parameters = aruco.DetectorParameters_create()
        parameters.adaptiveThreshConstant = 10
        corners, ids, rejectedImgPoints = aruco.detectMarkers(image, aruco_dict,
                                                            parameters=parameters,
                                                            cameraMatrix=self.mtx,
                                                            distCoeff=self.dist)


        if np.all(ids is not None):
            for i in range(0, len(ids)):
                aruco.drawDetectedMarkers(frame, corners)
                rvec, tvec ,_ = aruco.estimatePoseSingleMarkers(corners, 8.0, self.mtx, self.dist)

            return rvec, tvec, ids
        else:
            return [],[],0

    def compositeArray(self,rvec, tvec):
        v = np.c_[rvec, tvec.T]
        v_ = np.r_[v, np.array([[0,0,0,1]])]
        return v_

    def draw_cube(self,rvec,tvec, ids):
        alpha = self.mtx[0][0]
        beta = self.mtx[1][1]
        cx = self.mtx[0][2]
        cy = self.mtx[1][2]
        f = 1000.0
        n = 1.0

        view = np.array([
        [(alpha)/cx, 0,       0,                0 ],
        [0,          beta/cy, 0,                0 ],
        [0,          0,       -(f+n)/(f-n),     -1],
        [0,          0,       (-2.0*f*n)/(f-n), 0 ],
        ])

        glLoadMatrixd(view.T)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glPushMatrix()

        if not ids is None:
            tvec[0][0][0] = tvec[0][0][0]
            tvec[0][0][1] = -tvec[0][0][1]
            tvec[0][0][2] = -tvec[0][0][2]

            rvec[0][0][1] = -rvec[0][0][1]
            rvec[0][0][2] = -rvec[0][0][2]

            m = self.compositeArray(cv2.Rodrigues(rvec)[0], tvec[0][0])
            glPushMatrix()
            glLoadMatrixd(m.T)
            glColor3f(0.0,0.5,1.0)
            glutSolidCube(10.0)
            glPopMatrix()

        glPopMatrix()

        glFlush();
        glutSwapBuffers()


    def cap_texture(self):
        red,frame = cap.read() #aktuális kamera kép

        image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) #átkell konvertálni
        heightI, widthI = image.shape[:2] # a szélesség és magasság paramétereket így kapjuk meg
        rvec, tvec,ids = self.find_aruco(image)
        if(rvec != []):
            aruco.drawAxis(image, self.mtx, self.dist, rvec, tvec, 0.7)
        #textúra készítés a képből
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, widthI, heightI, 0, GL_RGB, GL_UNSIGNED_BYTE, image)

        #textúrázáshoz szükséges dolgok:
        glDisable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(1.0, 1.0, 1.0)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        #hatter kirajzolása:
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

        glEnable(GL_DEPTH_TEST)
        glDisable(GL_TEXTURE_2D)

        if(rvec != []):
            self.draw_cube(rvec,tvec,ids)
        glutPostRedisplay()
        glFlush()
        glutSwapBuffers()

    def keyboardF(self,key,x,y):
        if key == b'\x1b':
            sys.exit()

    def main(self):
        glutInit()
        glutInitWindowPosition(self.x, self.y)
        glutInitWindowSize(self.width,self.height)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutCreateWindow("Track aruco and draw a cube")
        self.mtx,self.dist = self.load_coefficients("log.json")
        glutDisplayFunc(self.cap_texture)
        glutKeyboardFunc(self.keyboardF)
        glutMainLoop()
        
cube = Cube()
cube.main()
