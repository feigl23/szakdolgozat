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
gluPerspective(90.0, width/float(height), 1, 500.0)

glMatrixMode(GL_MODELVIEW)

glEnable(GL_DEPTH_TEST)

rx, ry = (0,150)
tx, ty = (100,-200)
zpos = 0
rotate = move = False
peng_x = -5
peng_y = -20
peng_z = 20
peng_rot_z = 0


def compositeArray(rvec, tvec):
    v = np.c_[rvec, tvec.T]
    #print(v)
    v_ = np.r_[v, np.array([[0,0,0,1]])]
    return v_


def drawn_background(frame, mtx, rvec, tvec):

                alpha = mtx[0][0]
                beta = mtx[1][1]
                cx = mtx[0][2]
                cy = mtx[1][2]
                img= cv2.cvtColor(frame.astype("float32"),cv2.COLOR_BGRA2RGB ) #BGR-->RGB

                h, w = img.shape[:2]
                glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, w, h, 0, GL_RGB, GL_UNSIGNED_BYTE, img)

                glDisable(GL_DEPTH_TEST)
                glDisable(GL_LIGHTING)
                glDisable(GL_LIGHT0)
                glEnable(GL_TEXTURE_2D)

                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                glColor3f(1.0, 1.0, 1.0)
                glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
                glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)


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

                ## make projection matrix
                f = 1000.0
                n = 1.0

                m1 = np.array([
                [(alpha)/cx, 0,       0,            0               ],
                [0,          beta/cy, 0,            0               ],
                [0,          0,       -(f+n)/(f-n), (-2.0*f*n)/(f-n)],
                [0,          0,       -1,           0               ]],dtype=float)
                #glLoadTransposeMatrixd(m1.T)

                glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [0.0,0.0,1.0,1.0])
                tvec[0][0][0] = tvec[0][0][0]
                tvec[0][0][1] = -tvec[0][0][1]
                tvec[0][0][2] = -tvec[0][0][2]

                rvec[0][0][1] = -rvec[0][0][1]
                rvec[0][0][2] = -rvec[0][0][2]
                m = compositeArray(cv2.Rodrigues(rvec)[0], tvec[0][0])
                glPushMatrix()

                glLoadTransposeMatrixd(m.T)
                glPopMatrix()
                glFlush();
                #drawn(rx, ry, tx, ty, zpos, rotate,  move, peng_x , peng_y ,peng_z , peng_rot_z)
                #glutSwapBuffers()
                #cv2.imshow('frame',img)
def drawn(rx, ry, tx, ty, zpos, rotate,  move, peng_x , peng_y ,peng_z , peng_rot_z,frame, mtx, rvec, tvec):

    clock.tick(30)
    drawn_background(frame, mtx, rvec, tvec)
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
    glTranslate(5., -10., - 0)
    glRotate(150, 1, 0, 0)
    glRotate(0, 0, 1, 0)


    for i in range(20):
        glPushMatrix();
        glTranslate(-24+(2*i), 33, 15)
        box[i].render()
        glPopMatrix();
    for i in range(20, 38):
        glPushMatrix();
        glTranslate(-62+(i*2), 31, 15)
        box[i].render()
        glPopMatrix();
    for i in range(38, 54):
        glPushMatrix();
        glTranslate(-97+(2*i), 29, 15)
        box[i].render()
        glPopMatrix();
    for i in range(54, 66):
        glPushMatrix();
        glTranslate(-124+(i*2), 27, 15)
        box[i].render()
        glPopMatrix();
    for i in range(66,74):
        glPushMatrix();
        glTranslate(-144+(2*i), 25, 15)
        box[i].render()
        glPopMatrix();
    for i in range(74, 78):
        glPushMatrix();
        glTranslate(-156+(i*2), 23, 15)
        box[i].render()
        glPopMatrix();
    for i in range(78, 80):
        glPushMatrix();
        glTranslate(-162+(i*2), 21, 15)
        box[i].render()
        glPopMatrix();
    for i in range(80, 81):
        glPushMatrix();
        glTranslate(-165+(i*2), 19, 15)
        box[i].render()
        glPopMatrix();

    glPushMatrix()

    glTranslate(-5, -35, 40)
    glRotate(180+rx, 0, 0, 1)
    glRotate(180, 1, 0, 0)

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
