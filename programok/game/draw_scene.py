# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *
from box import *
from blue import *
from lilac import *
from castle import *

class Game:
    def __init__(self):
        self.blue = Blue()
        self.lilac = Lilac()
        self.castle = Castle()
        self.box = Box()
        self.x =0
        self.y=0
        self.z =-30

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
        self.castle.model_init()
        self.lilac.model_init()
        self.blue.model_init()
        self.box.load_lilac()
        self.box.load_blue()


    def draw_model(self):
            glClearColor(0.8, 0.8, 1.0, 0.0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            glTranslate(self.x,self.y,self.z)
            glEnable(GL_TEXTURE_2D)
            self.castle.draw_model()
            self.lilac.draw_model()
            self.blue.draw_model()
            self.box.draw_models()
            glutPostRedisplay()
            glutSwapBuffers()

    def keyboardF(self,key,x,y):
        if key == b'\x1b':
          sys.exit()
        elif key == b'a':
            if(self.blue.rot_z==360):
                self.blue.rot_z -=90
            elif(self.blue.rot_z==-360):
                self.blue.rot_z +=90
            else:
                self.blue.rot_z -=90
        elif key == b'w':
            if self.blue.rot_z == 90:
                self.blue.x-=0.5
            elif self.blue.rot_z == 180:
                self.blue.y-=0.5
            elif self.blue.rot_z ==-180:
                self.blue.y +=0.5
            elif self.blue.rot_z == 270:
                self.blue.x +=0.5
            elif self.blue.rot_z == -90:
                self.blue.x-=0.5
            elif self.blue.rot_z == -270:
                self.blue.x+=0.5
            else:
                self.blue.y += 0.5
        elif key == b's':
            if  self.blue.rot_z == -90:
                self.blue.x+=0.5
            elif  self.blue.rot_z == 180:
                self.blue.y+=0.5
            elif self.blue.rot_z == -180:
                self.blue.x -=0.5
            elif  self.blue.rot_z == -270:
                self.blue.x+=0.5
            elif  self.blue.rot_z == 90:
                self.blue.x+=0.5
            elif  self.blue.rot_z == 270:
                self.blue.x-=0.5
            else:
                self.blue.y-=0.5
        elif key ==  b'd':
            if(self.blue.rot_z==-360):
                self.blue.rot_z +=90
            elif(self.blue.rot_z== 360):
                self.blue.rot_z -=90
            else:
                self.blue.rot_z +=90

    def arrows(self,key, x, y):
        if key == GLUT_KEY_LEFT:
            if(self.lilac.rot_z==360):
                self.lilac.rot_z -=90
            elif(self.lilac.rot_z==-360):
                self.lilac.rot_z +=90
            else:
                self.lilac.rot_z -=90
        elif key == GLUT_KEY_UP:
            if self.lilac.rot_z == 90:
                self.lilac.x+=0.5
            elif self.lilac.rot_z == 180 or self.lilac.rot_z ==-180:
                self.lilac.y+=0.5
            elif self.lilac.rot_z == 270:
                self.lilac.x -=0.5
            elif self.lilac.rot_z == -90:
                self.lilac.x-=0.5
            elif self.lilac.rot_z == -270:
                self.lilac.x-=0.5
            else:
                self.lilac.y -= 0.5
        elif key == GLUT_KEY_DOWN:
            if  self.lilac.rot_z == -90:
                self.lilac.x+=0.5
            elif  self.lilac.rot_z == 180 or  self.lilac.rot_z == -180 :
                self.lilac.y-=0.5
            elif  self.lilac.rot_z == -270:
                self.lilac.x-=0.5
            elif  self.lilac.rot_z == 90:
                self.lilac.x-=0.5
            elif  self.lilac.rot_z == 270:
                self.lilac.x+=0.5
            else:
                self.lilac.y+=0.5
        elif key == GLUT_KEY_RIGHT:
            if(self.lilac.rot_z==-360):
                self.lilac.rot_z +=90
            elif(self.lilac.rot_z==360):
                self.lilac.rot_z -=90
            else:
                self.lilac.rot_z +=90

    def main(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowPosition(300, 150)
        glutInitWindowSize(640,480)
        glutCreateWindow("Game")
        glutKeyboardFunc(self.keyboardF)
        glutSpecialFunc(self.arrows)
        self.init()
        glutDisplayFunc(self.draw_model)
        glutMainLoop()


game = Game()
game.main()
