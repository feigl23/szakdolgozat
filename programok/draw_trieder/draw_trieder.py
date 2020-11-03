# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Trieder:
    def __init__(self):
        self.model = None

    def init(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(90.0, float(640)/float(480), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
 

    def draw_trieder(self):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            glTranslate(0,0,-10)
            # Hogy latszodjon a kek is: a felso glTranslate() helyett:
            #glTranslate(0,-8,-10)
            #glRotate(90,0,1,1)
            glBegin(GL_LINES)
            glColor3f(1, 0, 0)
            glVertex3f(0, 0, 0)
            glVertex3f(10, 0, 0)

            glColor3f(0, 1, 0)
            glVertex3f(0, 0, 0)
            glVertex3f(0, 10, 0)

            glColor3f(0, 0, 1)
            glVertex3f(0, 0, 0)
            glVertex3f(0, 0, 10)
            glEnd()
            glutSwapBuffers()

    def keyboardF(self,key,x,y):
        if key == b'\x1b':
          sys.exit()

    def main(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowPosition(300, 150);
        glutInitWindowSize(640,480);
        glutCreateWindow("Load object")
        glutKeyboardFunc(self.keyboardF)
        self.init()
        glutDisplayFunc(self.draw_trieder)
        glutMainLoop()


trieder = Trieder()
trieder.main()
