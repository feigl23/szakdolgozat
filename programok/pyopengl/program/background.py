from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import cv2
import cv2. aruco as aruco

class Background:

    def __init__(self):
        self.texture_background = None
        self.image = None

    def gentext(self):
        self.texture_background = glGenTextures(1)

    def make_bg_text(self,frame, run, mtx, dist,rvec, tvec):
        self.image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        heightI, widthI = self.image.shape[:2]
        if(run):
            aruco.drawAxis(self.image, mtx, dist, rvec, tvec, 0.1)

        glBindTexture(GL_TEXTURE_2D, self.texture_background)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, widthI, heightI, 0, GL_RGB, GL_UNSIGNED_BYTE, self.image)
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

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glDisable(GL_TEXTURE_2D)

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
