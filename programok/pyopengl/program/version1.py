# -*- coding: utf-8 -*-
import cv2
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *
import numpy as np
import cv2.aruco as aruco


class Penguin:
    def __init__(self):
        self.webcam = cv2.VideoCapture(0)
        self.penguin = None
        self.view_matrix = np.array([])
        self.bg_text= None

    def init(self):
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glEnable(GL_COLOR_MATERIAL)
        glLightfv(GL_LIGHT0, GL_POSITION,  (100, 100, 100, 0.0))
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.2, 1.0))

        self.penguin=OBJ("../models/Penguin/PenguinBaseMesh.obj", swapyz=True)
        self.penguin.generate()
        glEnable(GL_TEXTURE_2D)
        self.texture_background = glGenTextures(1)
    def keyboardF(self,key,x,y):
        if key == b'\x1b':
          sys.exit()

    def compositeArray(self,rvec, tvec):
        v = np.c_[rvec, tvec.T]
        #print(v)
        v_ = np.r_[v, np.array([[0,0,0,1]])]
        return v_
    def find_aruco(self, frame):
        matrix_coefficients, distortion_coefficients = self.load_coefficients("log.txt")
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_100)
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
                return rvec, tvec, matrix_coefficients, distortion_coefficients, ids
        else:
            return [], [], matrix_coefficients, distortion_coefficients, ids

    def draw_obj(self, rvec, tvec, mtx, dst, ids):
        alpha = mtx[0][0]
        beta = mtx[1][1]
        cx = mtx[0][2]
        cy = mtx[1][2]
        f = 1000.0
        n = 1.0

        m1 = np.array([
            [(alpha)/cx, 0,       0,            0               ],
            [0,          beta/cy, 0,            0               ],
            [0,          0,       -(f+n)/(f-n), (-2.0*f*n)/(f-n)],
            [0,          0,       -1,           0               ],
        ])
        glLoadTransposeMatrixd(m1.T)

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

            glLoadTransposeMatrixd(m.T)

            glPushMatrix()


            glPushMatrix()
            glEnable(GL_TEXTURE_2D)
            glRotatef(180,1,0,0)
            #glTranslatef(0,0,-20)
            #glTranslatef(0,0,0)
            glScalef(4,4,4)
            #glBegin(GL_LINES)
            #glColor3f(1, 0, 0)
            #glVertex3f(0, 0, 0)
            #glVertex3f(-50, 0, 0)

            #glColor3f(0, 1, 0)
            #glVertex3f(0, 0, 0)
            #glVertex3f(0, -50, 0)

            #glColor3f(0, 0, 1)
            #glVertex3f(0, 0, 0)
            #glVertex3f(0, 0, -50)
            #glEnd()
            self.penguin.render()
            glPopMatrix()
            glPopMatrix()

        glPopMatrix()

    def load_coefficients(self,path):

        cv_file = cv2.FileStorage(path, cv2.FILE_STORAGE_READ)

        camera_matrix = cv_file.getNode("K").mat()
        dist_matrix = cv_file.getNode("D").mat()

        cv_file.release()
        return [camera_matrix, dist_matrix]

    def cap_texture(self):
        red,frame = self.webcam.read() #aktuális kamera kép

        image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) #átkell konvertálni
        heightI, widthI = image.shape[:2] # a szélesség és magasság paramétereket így kapjuk meg
        #textúra készítés a képből
        rvec, tvec, mtx, dst, ids= self.find_aruco(frame)
        if(rvec != []):
            aruco.drawAxis(image, mtx, dst, rvec, tvec, 0.1)
        glBindTexture(GL_TEXTURE_2D, self.texture_background)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, widthI, heightI, 0, GL_RGB, GL_UNSIGNED_BYTE, image)

        # draw background
        glBindTexture(GL_TEXTURE_2D, self.texture_background)

        #textúrázáshoz szükséges dolgok:
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
        glEnable(GL_TEXTURE_2D)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(1.0, 1.0, 1.0)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        #hatter kirajzolása:
        self.draw_background()


        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glDisable(GL_TEXTURE_2D)
        if(rvec != []):
            self.draw_obj(rvec, tvec, mtx, dst, ids)
        glutPostRedisplay()
        glFlush();
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



    def main(self):
        glutInit()
        glutInitWindowPosition(300, 150);
        glutInitWindowSize(640,480);
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutCreateWindow("Window with camera image texture and a obj")
        glutKeyboardFunc(self.keyboardF)
        self.init()
        glutDisplayFunc(self.cap_texture)
        glutMainLoop()

Penguin = Penguin()
Penguin.main()
