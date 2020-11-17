# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *
import random

class DrawScene:
    def __init__(self):
        self.penguin = None
        self.castle = None
        self.box = []
        self.psyduck = None
        self.x =0
        self.y=0
        self.z =-60

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
        self.penguin=OBJ("models/Penguin/PenguinBaseMesh.obj", swapyz=True)
        self.castle=OBJ("models/Castle/CastleOBJ.obj", swapyz=True)
        self.psyduck=OBJ("models/psyduck/psyduck.obj", swapyz=True)
        for i in range(0,40):
            self.box.append(OBJ("models/Crate/Crate1.obj", swapyz=True))
            self.box[i].generate()
        self.castle.generate()
        self.penguin.generate()
        self.penguin.generate()

    def draw_model(self):
            glClearColor(0.8, 0.8, 1.0, 0.0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            glTranslate(self.x,self.y,self.z)
            self.castle.render()
            glPushMatrix()
            glScale(5,5,5)
            glTranslate(0,-1,0)
            #glRotate(180,0,0,1)
            glPushAttrib(GL_CURRENT_BIT)
            glColor(0,0.8,1)
            self.penguin.render()
            glPopAttrib()
            glPopMatrix()
            glPushMatrix()
            glScale(5,5,5)
            glTranslate(0,3.5,0)
            glPushAttrib(GL_CURRENT_BIT)
            glColor(1,0,1)
            glRotate(-180,0,0,1)
            self.penguin.render()
            glPopAttrib()
            glPopMatrix()
            d=-22
            k = -22
            for i in range(0,10):
                glPushMatrix()
                glPushAttrib(GL_CURRENT_BIT)
                glColor(1,0,1)
                d+=4
                glTranslate(d,-2,0)
                self.box[i].render()
                glPopAttrib()
                glPopMatrix()
            for i in range(10,20):
                glPushMatrix()
                glPushAttrib(GL_CURRENT_BIT)
                glColor(0,0.8,1)
                k+=4
                glTranslate(k,13,0)
                self.box[i].render()
                glPopAttrib()
                glPopMatrix()

            glutPostRedisplay()
            glutSwapBuffers()

    def keyboardF(self,key,x,y):
        if key == b'\x1b':
          sys.exit()
        elif key ==b'w':
            self.y -=1
        elif key == b's':
            self.y+=1

    def arrows(self,key, x, y):
        if key == GLUT_KEY_LEFT:
            self.x +=1
        elif key == GLUT_KEY_UP:
            self.z += 1
        elif key == GLUT_KEY_DOWN:
            self.z -= 1
        elif key == GLUT_KEY_RIGHT:
            self.x -=1

    def main(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowPosition(300, 150)
        glutInitWindowSize(640,480)
        glutCreateWindow("Draw scene")
        glutKeyboardFunc(self.keyboardF)
        glutSpecialFunc(self.arrows)
        self.init()
        glutDisplayFunc(self.draw_model)
        glutMainLoop()


draw_scene = DrawScene()
draw_scene.main()
