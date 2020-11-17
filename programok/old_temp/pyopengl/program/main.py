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
from background import *
from drawscene import *

class arGame:
    def __init__(self):
        self.camera = Camera()
        self.calibration = Calibration()
        self.track = Track()
        self.scene = DrawScene()
        self.background = Background()
        #self.view_matrix = np.array([])

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
        self.calibration.calibrate("images","image","png",0.015,6,9)
        self.scene.init()
        glEnable(GL_TEXTURE_2D)
        self.background.gentext()

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



    def display(self):

        frame = self.camera.get_frame()
        self.track.find_aruco(frame,  self.calibration.mtx, self.calibration.dist)

        self.background.make_bg_text(frame, self.track.run, self.calibration.mtx, self.calibration.dist, self.track.rvec, self.track.tvec)

        if(self.track.run):
            self.scene.view(self.calibration.mtx, self.track.rvec, self.track.tvec, self.track.ids)

        glutPostRedisplay()
        glFlush() 
        glutSwapBuffers()

    def main(self):
        glutInit()
        glutInitWindowPosition(300, 150) 
        glutInitWindowSize(640,480) 
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutCreateWindow("Window with camera image texture and a obj")
        glutKeyboardFunc(self.keyboardF)
        glutSpecialFunc(self.arrows)
        self.initsc()
        glutDisplayFunc(self.display)
        #glutIdleFunc(self.display)
        glutMainLoop()

arGame=arGame()
arGame.main()
