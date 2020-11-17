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
from tracker import *
from draw_background import *
from camera import *
from constans import *
import cv2


cap = cv2.VideoCapture(0)
class Game:
    def __init__(self):
        self.blue = Blue()
        self.lilac = Lilac()
        self.castle = Castle()
        self.box = Box()
        self.collision = Collision()
        self.keyboard = Keyboard()
        self.direct_animation = DirectAnim()
        self.traker = Traker()
        self.camera = Camera()
        self.background = Background()
        self.constans = Constans()
        self.x =0
        self.y=0
        self.z =-40
        self.run_lilac = False
        self.run_blue = False
        self.anim = False
        self.is_not_end = True
        self.mtx = None
        self.dist = None
        self.texture_background = None
        self.view = None
        self.frame = None
        self.rvec = []
        self.tvec = []

    def init(self):
        glClearColor(0.8, 0.8, 1.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(90, float(640)/float(480), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        self.castle.model_init()
        self.lilac.model_init()
        self.blue.model_init()
        self.box.load_boxes()
        self.view,self.mtx,self.dist = self.constans.get_matrix()
        glEnable(GL_TEXTURE_2D)
        self.texture_background = glGenTextures(1)


    def capture(self):
        s,self.frame = cap.read()
        self.rvec,self.tvec, self.ids = self.traker.track(self.frame, self.mtx, self.dist)
        self.background.draw(self.frame,self.dist, self.mtx,self.texture_background,self.rvec, self.tvec)
        if(self.rvec !=[]):
            self.draw_scene()
        glutPostRedisplay()
        glFlush()
        glutSwapBuffers()

    def draw_scene(self):
        if(self.box.is_over):
            glClearColor(0.8, 0.8, 1.0, 0.0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            print("VÉGE")
        else:
            if(self.anim == False):
                glEnable(GL_DEPTH_TEST)
                glDisable(GL_TEXTURE_2D)
                glLoadMatrixd(self.view.T)

                glMatrixMode(GL_MODELVIEW)
                glLoadIdentity()


                if not self.ids is None:
                    self.tvec[0][0][0] = self.tvec[0][0][0]
                    self.tvec[0][0][1] = -self.tvec[0][0][1]
                    self.tvec[0][0][2] = -self.tvec[0][0][2]

                    self.rvec[0][0][1] = -self.rvec[0][0][1]
                    self.rvec[0][0][2] = -self.rvec[0][0][2]

                    rot_m = self.constans.compositeArray(cv2.Rodrigues(self.rvec)[0], self.tvec[0][0])
                    glPushMatrix()
                    glLoadMatrixd(rot_m.T)
                    #glTranslate(self.x,self.y,self.z)
                    self.castle.draw_model()
                    self.blue.draw_model()
                    self.lilac.draw_model()
                    self.box.draw_models()
                    glPopMatrix()
                glutPostRedisplay()
                glutSwapBuffers()
            else:
                self.is_not_end =True
                self.anim = self.direct_animation.direct(self)

    def keyboardF(self,key,x,y):
        if key == b'\x1b':
             sys.exit()
        self.keyboard.keyboardF(self,key)

    def main(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowPosition(300, 150)
        glutInitWindowSize(640,480)
        glutCreateWindow("Game")
        glutKeyboardFunc(self.keyboardF)
        self.init()
        glutDisplayFunc(self.capture)
        glutMainLoop()


game = Game()
game.main()
