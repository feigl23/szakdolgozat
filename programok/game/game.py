# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *
from box import *
from blue import *
from lilac import *
from castle import *
from collision import *
from keyboard import *
from direct_animation import *

class Game:
    def __init__(self):
        self.blue = Blue()
        self.lilac = Lilac()
        self.castle = Castle()
        self.box = Box()
        self.collision = Collision()
        self.keyboard = Keyboard()
        self.direct_animation = DirectAnim()
        self.x =0
        self.y=0
        self.z =-30
        self.run_lilac = False
        self.run_blue = False
        self.anim = False
        self.is_end = True

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


    def draw_scene(self):
        if(self.anim == False):
            glClearColor(0.8, 0.8, 1.0, 0.0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            glTranslate(self.x,self.y,self.z)
            self.castle.draw_model()
            self.blue.draw_model()
            self.lilac.draw_model()
            self.box.draw_models()
            glutPostRedisplay()
            glutSwapBuffers()
        else:
            self.is_end =True
            self.anim = self.direct_animation.direct(self)

    def arrows(self,key,x,y):
        self.keyboard.arrows(self,key)

    def keyboardF(self,key,x,y):
        self.keyboard.keyboardF(self,key)

    def main(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowPosition(300, 150)
        glutInitWindowSize(640,480)
        glutCreateWindow("Game")
        glutKeyboardFunc(self.keyboardF)
        glutSpecialFunc(self.arrows)
        self.init()
        glutDisplayFunc(self.draw_scene)
        glutMainLoop()


game = Game()
game.main()
