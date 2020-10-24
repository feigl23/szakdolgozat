#!/usr/bin/env python

import sys, pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# IMPORT OBJECT LOADER
from objloader import *

import cv2
import numpy as np
from PIL import Image

pygame.init()
viewport = (1000,550)
hx = viewport[0]/3
hy = viewport[1]/3
srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)

cap = cv2.VideoCapture(0)

glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 100, 100, 0.0))
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.2, 1.0))
glEnable(GL_LIGHT0)
glEnable(GL_LIGHTING)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_DEPTH_TEST)
glShadeModel(GL_SMOOTH)           # most obj files expect to be smooth-shaded

# LOAD OBJECT AFTER PYGAME INIT
obj1 = OBJ("models/Penguin/PenguinBaseMesh.obj", swapyz=True)
obj1.generate()
obj3 = OBJ("models/Castle/CastleOBJ.obj", swapyz=True)
obj3.generate()
#obj2 = OBJ("models/OBJ/Tropical Islands.obj", swapyz=True)
box = []

for i in range (100):
    box.append(OBJ("models/Crate/Crate1.obj", swapyz=True))
    box[i].generate()

 #obj4 = OBJ('models/cube/cube.obj', swapyz=True)

#obj4.generate();
obj4 = gluNewQuadric()

clock = pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
glLoadIdentity()

width, height = viewport
gluPerspective(90.0, width/float(height), 1, 1000.0)

glMatrixMode(GL_MODELVIEW)

glEnable(GL_DEPTH_TEST)

rx, ry = (0,150)
tx, ty = (100,-200)
zpos = 0
rotate = move = False
peng_x = -5
peng_y = -32
peng_z = 20
peng_rot_z = 0


while 1:
    clock.tick(30)
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit()
        elif e.type == KEYDOWN and e.key == K_ESCAPE:
            sys.exit()
        elif e.type == MOUSEBUTTONDOWN:
            if e.button == 4: zpos = max(1, zpos-1)
            elif e.button == 5: zpos += 1
            elif e.button == 1: rotate = True
            elif e.button == 3: move = True
        elif e.type == MOUSEBUTTONUP:
            if e.button == 1: rotate = False
            elif e.button == 3: move = False
        elif e.type == MOUSEMOTION:
            i, j = e.rel
            if rotate:
                rx += i
                ry += j
        elif e.type == KEYDOWN and e.key == K_LEFT:
                peng_rot_z +=90
        elif  e.type == KEYDOWN and e.key == K_RIGHT:
                peng_rot_z -=90
        elif e.type == KEYDOWN and e.key == K_UP:
                if peng_rot_z == 90:
                    peng_x+=0.5
                elif peng_rot_z == 180 or peng_rot_z ==-180:
                    peng_z-=0.5
                elif peng_rot_z == 270:
                    peng_x -=0.5
                elif peng_rot_z == -90:
                    peng_x-=0.5
                elif peng_rot_z == -270:
                    peng_x+=0.5
                else:
                    peng_z += 0.5
        elif e.type == KEYDOWN and e.key == K_DOWN:
                if peng_rot_z == -90:
                    peng_x+=0.5
                elif peng_rot_z == 180 or peng_rot_z == -180 :
                    peng_z+=0.5
                elif peng_rot_z == -270:
                    peng_x-=0.5
                elif peng_rot_z == 90:
                    peng_x-=0.5
                elif peng_rot_z == 270:
                    peng_x+=0.5
                else:
                    peng_z-=0.5
        elif e.type == KEYDOWN and e.key == K_SPACE:
                    peng_y +=0.5





    keypress = pygame.key.get_pressed()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    # RENDER OBJECT

    glLoadIdentity()

    for i in range(20):
        glPushMatrix();
        glTranslate(-24+(2*i), -33, 15)
        box[i].render()
        glPopMatrix();
    for i in range(20, 38):
        glPushMatrix();
        glTranslate(-62+(i*2), -31, 15)
        box[i].render()
        glPopMatrix();
    for i in range(38, 54):
        glPushMatrix();
        glTranslate(-97+(2*i), -29, 15)
        box[i].render()
        glPopMatrix();
    for i in range(54, 66):
        glPushMatrix();
        glTranslate(-124+(i*2), -27, 15)
        box[i].render()
        glPopMatrix();
    for i in range(66,74):
        glPushMatrix();
        glTranslate(-144+(2*i), -25, 15)
        box[i].render()
        glPopMatrix();
    for i in range(74, 78):
        glPushMatrix();
        glTranslate(-156+(i*2), -23, 15)
        box[i].render()
        glPopMatrix();
    for i in range(78, 80):
        glPushMatrix();
        glTranslate(-162+(i*2), -21, 15)
        box[i].render()
        glPopMatrix();
    for i in range(80, 81):
        glPushMatrix();
        glTranslate(-165+(i*2), -19, 15)
        box[i].render()
        glPopMatrix();

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
    obj3.render()

    glPopMatrix();

    glPushMatrix()
    if(peng_rot_z == 360 or peng_rot_z ==-360):
        peng_rot_z =0
    glTranslatef(peng_x,peng_y,peng_z)
    glRotate(peng_rot_z,0, 1, 0)
    glRotate(-90,1, 0, 0)
    glRotate(-180,0, 1, 0)
    glScale(3,3,3)
    obj1.render()
    glPopMatrix();



    pygame.display.flip()
    pygame.time.wait(10)
