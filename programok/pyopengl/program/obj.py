# -*- coding: utf-8 -*-
import cv2
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *
import numpy as np

from camera import *
from track import *
from calibration import *
from penguin import *
from castle import *
from box import *

class DrawScene:
    def __init__(self):
        self.camera = Camera()
        self.calibration = Calibration()
        self.track = Track()
        self.penguin = None
        self.view_matrix = np.array([])
        self.bg_text= None
        self.penguin = Penguin()
        self.castle = Castle()
        self.box = Box()

    def initsc(self):
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


        glEnable(GL_TEXTURE_2D)
        self.texture_background = glGenTextures(1)
        self.castle.model.generate()
        self.penguin.model.generate()
        self.calibration.calibrate("images","image","png",0.015,6,9)


    def keyboardF(self,key,x,y):
        if key == b'\x1b':
          sys.exit()

    def arrows(self,key, x, y):
        if key == GLUT_KEY_LEFT:
            self.penguin.model.rot_z +=90
        elif key == GLUT_KEY_UP:
            if self.penguin.model.rot_z == 90:
                self.penguin.model.x+=0.5
            elif self.penguin.model.rot_z == 180 or self.penguin.model.rot_z ==-180:
                self.penguin.model.z-=0.5
            elif self.penguin.model.z == 270:
                self.penguin.model.x -=0.5
            elif self.penguin.model.z == -90:
                self.penguin.model.x-=0.5
            elif self.penguin.model.z == -270:
                self.penguin.model.x+=0.5
            else:
                self.penguin.model.z += 0.5
        elif key == GLUT_KEY_DOWN:
            if self.penguin.model.z == -90:
                self.penguin.model.x+=0.5
            elif self.penguin.model.rot_z == 180 or self.penguin.model.rot_z == -180 :
                self.penguin.model.z+=0.5
            elif self.penguin.model.rot_z == -270:
                self.penguin.model.x-=0.5
            elif self.penguin.model.rot_z == 90:
                self.penguin.model.x-=0.5
            elif self.penguin.model.rot_z == 270:
                self.penguin.model.x+=0.5
            else:
                self.penguin.model.z-=0.5
        elif key == GLUT_KEY_RIGHT:
            self.penguin.model.rot_z -=90



    def compositeArray(self, rvec, tvec):
        v = np.c_[rvec, tvec.T]
        #print(v)
        v_ = np.r_[v, np.array([[0,0,0,1]])]
        return v_

    def draw_obj(self):
        mtx = self.calibration.mtx
        tvec = self.track.tvec
        rvec = self.track.rvec
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

        if not self.track.ids is None:
            tvec[0][0][0] = tvec[0][0][0]
            tvec[0][0][1] = -tvec[0][0][1]
            tvec[0][0][2] = -tvec[0][0][2]

            rvec[0][0][1] = -rvec[0][0][1]
            rvec[0][0][2] = -rvec[0][0][2]
            m = self.compositeArray(cv2.Rodrigues(rvec)[0], tvec[0][0])

            glLoadTransposeMatrixd(m.T)

            self.penguin.drawn()
        glPopMatrix()

    def cap_texture(self):
        frame = self.camera.get_frame()


        image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        heightI, widthI = image.shape[:2]

        self.track.find_aruco(frame)
        if(self.track.run):
            aruco.drawAxis(image, self.calibration.mtx, self.calibration.dist, self.track.rvec, self.track.tvec, 0.1)
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
        if(self.track.run):
            self.draw_obj()
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
        glutSpecialFunc(self.arrows)
        self.initsc()
        glutDisplayFunc(self.cap_texture)
        glutMainLoop()

DrawScene = DrawScene()
DrawScene.main()
