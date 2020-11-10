# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *
import time

class Jump:
    def __init__(self):
        self.d =1
        self.penguins = []

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
        for i in range(1,21):
            if(i<10):
                self.penguins.append(OBJ("models/RiggedPenguin_00000"+str(i)+".obj", swapyz=True))
            else:
                self.penguins.append(OBJ("models/RiggedPenguin_0000"+str(i)+".obj", swapyz=True))
            self.penguins[i-1].generate()
    def draw_model(self):
            for i in range(1,21):
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                glPushMatrix()
                glLoadIdentity()
                glTranslate(0,-0.8,-2)
                glRotate(-90,1,0,0)
                glRotate(-180,0,0,1)
                self.penguins[i-1].render()
                glPopMatrix()
                glutPostRedisplay()
                glutSwapBuffers()
                time.sleep(.01)

    def keyboardF(self,key,x,y):
        if key == b'\x1b':
          sys.exit()

    def main(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowPosition(300, 150)
        glutInitWindowSize(640,480)
        glutCreateWindow("Jump")
        glutKeyboardFunc(self.keyboardF)
        self.init()
        glutDisplayFunc(self.draw_model)
        glutMainLoop()


jump = Jump()
jump.main()
