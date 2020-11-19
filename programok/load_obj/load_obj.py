# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *


class LoadOBJ:
    def __init__(self):
        self.model = None

    def init(self):
        glClearColor(0.8, 0.8, 1.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLightfv(GL_LIGHT0, GL_POSITION,  (10, 10, 10, 10.0))
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.2, 1.0))
        glLoadIdentity()
        gluPerspective(90.0, float(640)/float(480), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        self.model=OBJ("models/Penguin/PenguinBaseMesh.obj", swapyz=True)
        self.model.generate()

    def draw_model(self):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            #glTranslate(0,-20,-60)
            glPushMatrix()
            #glRotate(180,0,1,0)
            #glScale(0.1,0.1,0.1)
            glTranslate(0,0,-2)
            self.model.render()
            glPopMatrix()
            glutSwapBuffers()

    def keyboardF(self,key,x,y):
        if key == b'\x1b':
          sys.exit()

    def main(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowPosition(300, 150)
        glutInitWindowSize(640,480)
        glutCreateWindow("Load object")
        glutKeyboardFunc(self.keyboardF)
        self.init()
        glutDisplayFunc(self.draw_model)
        glutMainLoop()


load= LoadOBJ()
load.main()
