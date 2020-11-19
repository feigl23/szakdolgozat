# -*- coding: utf-8 -*-
import cv2
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *


class Penguin:

    def __init__(self):
        self.webcam = cv2.VideoCapture(0)
        self.penguin = None

    def init(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(90, float(640)/float(480), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

        self.penguin=OBJ("models/Penguin/PenguinBaseMesh.obj", swapyz=True)
        self.penguin.generate()

    def keyboardF(self,key,x,y):
        if key == b'\x1b':
            sys.exit()

    def draw_obj(self):
        glEnable(GL_TEXTURE_2D)
        glLoadIdentity()

        glScale(0.3,0.3,0.3)
        glRotate(90,1,0,0)
        glRotate(180,0,1,0)
        glRotate(-180,0,0,1)
        glTranslatef(0,-3,0)

        self.penguin.render()

    def cap_texture(self):
        red,frame = self.webcam.read() #aktuális kamera kép

        image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) #átkell konvertálni
        heightI, widthI = image.shape[:2] # a szélesség és magasság paramétereket így kapjuk meg
        #textúra készítés a képből
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, widthI, heightI, 0, GL_RGB, GL_UNSIGNED_BYTE, image)

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
        self.draw_obj()
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

    def main(self):
        glutInit()
        glutInitWindowPosition(300, 150)
        glutInitWindowSize(640,480)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutCreateWindow("Window with camera image texture and a obj")
        glutKeyboardFunc(self.keyboardF)
        self.init()
        glutDisplayFunc(self.cap_texture)
        glutMainLoop()

Penguin = Penguin()
Penguin.main()
