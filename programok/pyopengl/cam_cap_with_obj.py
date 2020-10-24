# -*- coding: utf-8 -*-


import cv2
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *
cap = cv2.VideoCapture(0)
obj3 = OBJ("models/Penguin/PenguinBaseMesh.obj", swapyz=True)
x = 350
y = 150
width = 650
height = 500

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(33.7, 1.3, 0.1, 100.0)
    #gluPerspective(90, float(width)/float(height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def keyboardF(key,x,y):
    if key == b'\x1b':
      sys.exit()
def draw_obj():

    obj3.generate()
    #glPushMatrix()
    glScale(0.3,0.3,0.3)
    glRotate(90,1,0,0)
    glRotate(180,0,1,0)
    glRotate(-180,0,0,1)
    glTranslatef(0,-3,0)
    obj3.render()

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
    draw_background()

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glDisable(GL_TEXTURE_2D)
    draw_obj()
    glutPostRedisplay()
    glFlush();
    glutSwapBuffers()

def draw_background():
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

def main():
    glutInit()
    glutInitWindowPosition(x, y);
    glutInitWindowSize(width,height);
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutCreateWindow("Window with camera image texture and a cube")
    glutDisplayFunc(cap_texture)
    glutKeyboardFunc(keyboardF)
    init()
    glutMainLoop()

main()
