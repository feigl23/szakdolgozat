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
from timer import *
import cv2
import time


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
        self.timer = Timer()
        self.x =-2
        self.y=-4
        self.z =20
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
        self.i=0
        self.first=True
        self.was =0


    def init(self):
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
        if(self.anim == False):
            if(self.rvec !=[]):
                self.draw_scene()
            else:
                glutPostRedisplay()
                glutSwapBuffers()

        else:
            if(self.blue.length == self.lilac.length or self.blue.length>self.lilac.length):
                ido = 0.5/(self.blue.length*1000000000)
            else:
                ido = 0.5/(self.lilac.length*1000000000)
            if(self.first):
                self.first = False
                self.timer.start()

                game.i = 1
                self.direct_animation.direct(self)
                glutPostRedisplay()
                glutSwapBuffers()
                glFlush()
            else:
                if(self.timer.elapsed_time >= ido):
                    self.i+=1
                    self.timer.start()
                self.direct_animation.direct(self)
                glutPostRedisplay()
                glutSwapBuffers()
                glFlush()



    def draw_scene(self):
        if(self.box.is_over):
            if(self.was <3):
                self.was+=1
                glClearColor(0.8, 0.8, 1.0, 0.0)
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                bg =cv2.imread("images/win.jpg")
                self.background.draw(bg,self.dist, self.mtx,self.texture_background,[],[])
                glutPostRedisplay()
                glutSwapBuffers()
                glFlush()
            else:
                sys.exit()
        else:
                glEnable(GL_DEPTH_TEST)
                glDisable(GL_TEXTURE_2D)
                glLoadMatrixd(self.view)

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
                    glTranslate(self.x,self.y,self.z)

                    self.castle.draw_model()
                    self.blue.draw_model()
                    self.lilac.draw_model()
                    self.box.draw_models()
                    glPushMatrix()
                    glPushAttrib(GL_CURRENT_BIT)
                    if(self.box.right != True):
                        glTranslate(13,6,28)
                    if(self.box.left != True):
                        glTranslate(-13,6,29)
                    glColor4f(0.0,1.0,1.0,1)
                    glutSolidCube(5.8)
                    glPopAttrib()
                    glPopMatrix()
                    glPopMatrix()
                glutPostRedisplay()
                glutSwapBuffers()

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
