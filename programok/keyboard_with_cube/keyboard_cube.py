# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class KeyboardCube:
    def __init__(self):
        self.model = None
        self.x =0
        self.y=0
        self.z =-5
        self.rx =0
        self.ry =0

    def init(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLightfv(GL_LIGHT0, GL_POSITION,  (0, 0, -2, 2.0))
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.2, 1.0))
        glLoadIdentity()
        gluPerspective(90.0, float(640)/float(480), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)


    def draw_trieder(self):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            glTranslate(0,0,-5)
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
            glTranslate(self.x,self.y,self.z)
            glRotate(self.rx,1,0,0)
            glRotate(self.ry,0,1,0)
            glBegin(GL_QUADS)

            glColor3f(1.0,1.0,0.0)
            glVertex3f( 1.0, 1.0,-1.0)
            glVertex3f(-1.0, 1.0,-1.0)
            glVertex3f(-1.0, 1.0, 1.0)
            glVertex3f( 1.0, 1.0, 1.0)

            glColor3f(1.0,0.0,0.0)
            glVertex3f( 1.0,-1.0, 1.0)
            glVertex3f(-1.0,-1.0, 1.0)
            glVertex3f(-1.0,-1.0,-1.0)
            glVertex3f( 1.0,-1.0,-1.0)

            glColor3f(1.0,0.0,1.0)
            glVertex3f( 1.0, 1.0, 1.0)
            glVertex3f(-1.0, 1.0, 1.0)
            glVertex3f(-1.0,-1.0, 1.0)
            glVertex3f( 1.0,-1.0, 1.0)

            glColor3f(1.0,1.0,0.0)
            glVertex3f( 1.0,-1.0,-1.0)
            glVertex3f(-1.0,-1.0,-1.0)
            glVertex3f(-1.0, 1.0,-1.0)
            glVertex3f( 1.0, 1.0,-1.0)

            glColor3f(0.0,0.0,1.0)
            glVertex3f(-1.0, 1.0, 1.0)
            glVertex3f(-1.0, 1.0,-1.0)
            glVertex3f(-1.0,-1.0,-1.0)
            glVertex3f(-1.0,-1.0, 1.0)

            glColor3f(1.0,0.0,1.0)
            glVertex3f( 1.0, 1.0,-1.0)
            glVertex3f( 1.0, 1.0, 1.0)
            glVertex3f( 1.0,-1.0, 1.0)
            glVertex3f( 1.0,-1.0,-1.0)

            glEnd()
            glutPostRedisplay()
            glutSwapBuffers()

    def keyboardF(self,key,x,y):
        if key == b'\x1b':
          sys.exit()
        elif key == b' ':
          self.z +=1

    def arrows(self,key, x, y):
        if key == GLUT_KEY_LEFT:
            self.x -=1
        elif key == GLUT_KEY_UP:
            self.y += 1
        elif key == GLUT_KEY_DOWN:
            self.y -= 1
        elif key == GLUT_KEY_RIGHT: 
            self.x+=1

    def mouse(self,x,y):
        self.rx += x
        self.ry += y
         

    def main(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowPosition(300, 150);
        glutInitWindowSize(640,480);
        glutCreateWindow("Load object")
        glutKeyboardFunc(self.keyboardF)
        glutSpecialFunc(self.arrows)
        glutMotionFunc(self.mouse)
        self.init()
        glutDisplayFunc(self.draw_trieder)
        glutMainLoop()  


keyboardCube = KeyboardCube()
keyboardCube.main()
