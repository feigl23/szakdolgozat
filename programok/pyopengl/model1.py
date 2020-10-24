#!/usr/bin/env python
import sys
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import cv2
from objloader import *

cap = cv2.VideoCapture(0)
penguin = OBJ("models/Penguin/PenguinBaseMesh.obj", swapyz=True)
penguin.generate()
castle = OBJ("models/Castle/CastleOBJ.obj", swapyz=True)
castle.generate()
box = []

rx, ry = (0,150)
tx, ty = (100,-200)
zpos = 0
rotate = move = False
peng_x = -5
peng_y = -32
peng_z = 20
peng_rot_z = 0

for i in range (100):
    box.append(OBJ("models/Crate/Crate1.obj", swapyz=True))
    box[i].generate()

def init(width, height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90.0, float(width)/float(height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 100, 100, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.2, 1.0))
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)


    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
def draw_scene():
    #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    # RENDER OBJECT
    #glTranslate(60., -20., - 0)
    #glRotate(120, 1, 0, 0)
    #glRotate(0, 0, 1, 0)
    glPushMatrix()

    glTranslate(0, 0, 0)
    glRotate(-90+rx, 0, 0, 1)
    glRotate(-180, 1, 0, 0)

    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(-50, 0, 0)

    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, -50, 0)

    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, -50)
    glEnd()

    glColor3f(1, 1, 1)
    glutPostRedisplay()
    #castle.render()

    glPopMatrix();

    glPushMatrix()
    #if(peng_rot_z == 360 or peng_rot_z ==-360):
    #    peng_rot_z =0
    glTranslatef(peng_x,peng_y,peng_z)
    glRotate(peng_rot_z,0, 1, 0)
    glRotate(-90,1, 0, 0)
    glRotate(-180,0, 1, 0)
    glScale(3,3,3)
    glutPostRedisplay()
    #penguin.render()
    glPopMatrix();




def keyboard(key, x, y):
    if key == b'\x1b':
        sys.exit()

def arrows(key, x, y):

    if key == GLUT_KEY_LEFT:
        print("LEFT")
    elif key == GLUT_KEY_UP:
        print("UP")
    elif key == GLUT_KEY_DOWN:
        print("DOWN")
    elif key == GLUT_KEY_RIGHT:
        print("RIGHT")

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
    glFlush();
    glutSwapBuffers()

def main():
    x = 550
    y = 150
    width = 640
    height = 480
    glutInit()
    glutInitWindowPosition(x, y);
    glutInitWindowSize(width,height);
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutCreateWindow("Window with camera image texture")
    glutDisplayFunc(draw_scene)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(arrows)
    cap_texture()
    init(width, height)

    glutMainLoop()

main()
