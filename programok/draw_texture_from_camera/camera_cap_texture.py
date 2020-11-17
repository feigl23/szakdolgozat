# -*- coding: utf-8 -*-
import cv2
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

cap = cv2.VideoCapture(0)

x = 500
y = 150
width = 500
height = 500


def keyboardF(key,x,y):
    if key == b'\x1b':
      sys.exit()

def cap_texture():
    red,frame = cap.read() #aktuális kamera kép

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

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glDisable(GL_TEXTURE_2D)

    glutPostRedisplay()
    glFlush() 
    glutSwapBuffers()

def main():
    glutInit()
    glutInitWindowPosition(x, y) 
    glutInitWindowSize(width,height) 
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutCreateWindow("Window with camera image texture")
    glutDisplayFunc(cap_texture)
    glutKeyboardFunc(keyboardF)
    glutMainLoop()

main()
