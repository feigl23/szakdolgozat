# -*- coding: utf-8 -*-
#Felhasználva: https://rdmilligan.wordpress.com/2015/08/29/opencv-and-opengl-using-python/ (kocka)

import cv2
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

cap = cv2.VideoCapture(0)

x = 500
y = 150
width = 500
height = 500

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, float(width)/float(height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

def keyboardF(key,x,y):
    if key == b'\x1b':
      sys.exit()

def draw_cube():
    
        glPushMatrix()
        glClearDepth(1)
        glClearColor(0,0,0,0)
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity() 

        glScale(0.5,0.5,0.5)
        glRotatef(30,1.0,0.0,0.0)
        glRotatef(30,0.0,1.0,0.0)
        glRotatef(30,0.0,0.0,1.0)

        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)  glVertex3f(-1.0, -1.0,  1.0)
        glTexCoord2f(1.0, 0.0)  glVertex3f( 1.0, -1.0,  1.0)
        glTexCoord2f(1.0, 1.0)  glVertex3f( 1.0,  1.0,  1.0)
        glTexCoord2f(0.0, 1.0)  glVertex3f(-1.0,  1.0,  1.0)
        glTexCoord2f(1.0, 0.0)  glVertex3f(-1.0, -1.0, -1.0)
        glTexCoord2f(1.0, 1.0)  glVertex3f(-1.0,  1.0, -1.0)
        glTexCoord2f(0.0, 1.0)  glVertex3f( 1.0,  1.0, -1.0)
        glTexCoord2f(0.0, 0.0)  glVertex3f( 1.0, -1.0, -1.0)
        glTexCoord2f(0.0, 1.0)  glVertex3f(-1.0,  1.0, -1.0)
        glTexCoord2f(0.0, 0.0)  glVertex3f(-1.0,  1.0,  1.0)
        glTexCoord2f(1.0, 0.0)  glVertex3f( 1.0,  1.0,  1.0)
        glTexCoord2f(1.0, 1.0)  glVertex3f( 1.0,  1.0, -1.0)
        glTexCoord2f(1.0, 1.0)  glVertex3f(-1.0, -1.0, -1.0)
        glTexCoord2f(0.0, 1.0)  glVertex3f( 1.0, -1.0, -1.0)
        glTexCoord2f(0.0, 0.0)  glVertex3f( 1.0, -1.0,  1.0)
        glTexCoord2f(1.0, 0.0)  glVertex3f(-1.0, -1.0,  1.0)
        glTexCoord2f(1.0, 0.0)  glVertex3f( 1.0, -1.0, -1.0)
        glTexCoord2f(1.0, 1.0)  glVertex3f( 1.0,  1.0, -1.0)
        glTexCoord2f(0.0, 1.0)  glVertex3f( 1.0,  1.0,  1.0)
        glTexCoord2f(0.0, 0.0)  glVertex3f( 1.0, -1.0,  1.0)
        glTexCoord2f(0.0, 0.0)  glVertex3f(-1.0, -1.0, -1.0)
        glTexCoord2f(1.0, 0.0)  glVertex3f(-1.0, -1.0,  1.0)
        glTexCoord2f(1.0, 1.0)  glVertex3f(-1.0,  1.0,  1.0)
        glTexCoord2f(0.0, 1.0)  glVertex3f(-1.0,  1.0, -1.0)
        glEnd()
        glPopMatrix()

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
    draw_cube()
    glutPostRedisplay()
    glFlush() 
    glutSwapBuffers()

def main():
    glutInit()
    glutInitWindowPosition(x, y) 
    glutInitWindowSize(width,height) 
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutCreateWindow("Cube with camera image texture")
    glutDisplayFunc(cap_texture)
    glutKeyboardFunc(keyboardF)
    init()
    glutMainLoop()

main()
