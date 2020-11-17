# -*- coding: utf-8 -*-


import cv2
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import cv2.aruco as aruco
import numpy as np
from objloader import *



class Castle:
    def __init__(self):
        self.x = 500
        self.y = 150
        self.width =500
        self.height = 500
        self.mtx = None
        self.dist = None
        self.model = None
        self.texture_background = None

    def init(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(90, float(640)/float(480), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

        self.mtx,self.dist = self.load_coefficients("log.json")
        self.model=OBJ("models/Castle/CastleOBJ.obj", swapyz=True)
        self.model.generate()
        glEnable(GL_TEXTURE_2D)
        self.texture_background = glGenTextures(1)

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

    def draw_model(self,rvec,tvec, ids):
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
                glRotate(180,1,0,0)
                glRotate(-180,0,0,1)
                glTranslatef(0,0,-30)
                glEnable(GL_TEXTURE_2D)
                self.model.render()
                glDisable(GL_TEXTURE_2D)
                glPopMatrix()

            glPopMatrix()

            glFlush();
            glutSwapBuffers()


    def cap_texture(self):
        cap = cv2.VideoCapture(0)
        red,frame = cap.read()

        image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        heightI, widthI = image.shape[:2]
        rvec, tvec,ids = self.find_aruco(image)
        if(rvec != []):
            aruco.drawAxis(image, self.mtx, self.dist, rvec, tvec, 7)
        glBindTexture(GL_TEXTURE_2D, self.texture_background)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, widthI, heightI, 0, GL_RGB, GL_UNSIGNED_BYTE, image)

        glBindTexture(GL_TEXTURE_2D, self.texture_background)
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
        glEnable(GL_TEXTURE_2D)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(1.0, 1.0, 1.0)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        self.draw_background()
        glEnable(GL_DEPTH_TEST)     # Enable GL_DEPTH_TEST
        glDisable(GL_TEXTURE_2D)

        if(rvec != []):
            self.draw_model(rvec,tvec,ids)
        glutPostRedisplay()
        glFlush()
        glutSwapBuffers()

    def draw_background(self):
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


    def keyboardF(self,key,x,y):
        if key == b'\x1b':
            sys.exit()

    def main(self):
        glutInit()
        glutInitWindowPosition(self.x, self.y)
        glutInitWindowSize(self.width,self.height)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutCreateWindow("Track aruco and draw a castle model")
        self.init()
        glutDisplayFunc(self.cap_texture)
        glutKeyboardFunc(self.keyboardF)
        glutMainLoop()

castle = Castle()
castle.main()
