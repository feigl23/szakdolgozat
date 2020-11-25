from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *
from box import *
from penguin import *
from castle import *
from collision import *
from keyboard import *
from direct_draw import *
from tracker import *
from draw_background import *
from camera import *
from constans import *
from rest_reqs import *
from data import *
import cv2
import time

cap = cv2.VideoCapture(0)

class Game:
    def __init__(self):
        self.castle = Castle()
        self.penguins = []
        self.boxes = []
        self.max = 3
        self.box = 4*self.max
        for i in range(0,self.max):
            self.penguins.append(Penguin())
        for i in range(0,self.box):
            self.boxes.append(Box())
        self.collision = Collision()
        self.keyboard = Keyboard()
        self.direct = DirectDraw()
        self.traker = Traker()
        self.camera = Camera()
        self.background = Background()
        self.constans = Constans()
        self.requests = Requests()
        self.data = Data()
        self.user_id= self.requests.require_user_id()
        self.x =-2
        self.y=-4
        self.z =10
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
        self.own_model= None
        self.models_data = None

    def init(self):
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(90, float(640)/float(480), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        self.castle.model_init()
        for i in range(0,self.max):
            self.penguins[i].model_init()
        for i in range(0,self.box):
            self.boxes[i].model_init()
        self.view,self.mtx,self.dist = self.constans.get_matrix()
        glEnable(GL_TEXTURE_2D)
        self.texture_background = glGenTextures(1)
        if(self.user_id ==0):
            self.models_data = self.data.getdata()
            self.requests.upload_world_changes(self.models_data)
            self.own_model = self.models_data[str(self.user_id)]
        else:
            self.models_data = self.requests.require_world_state()
            self.own_model = self.models_data[str(self.user_id)]


    def capture(self):
        if(game.user_id ==0 ):
            castle = self.own_model['castle']
        else:
            castle =self.models_data['0']['castle']
        if(castle['fountain_box'] != self.box):
            self.models_data = self.requests.require_world_state()
            #print('New world:')
            #print(self.models_data)
            s,self.frame = cap.read()
            self.rvec,self.tvec, self.ids = self.traker.track(self.frame, self.mtx, self.dist)
            self.background.draw(self.frame,self.dist, self.mtx,self.texture_background,self.rvec, self.tvec)

            glEnable(GL_DEPTH_TEST)
            glDisable(GL_TEXTURE_2D)
            glLoadMatrixd(self.view)

            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            if not self.ids is None and self.rvec != []:
                self.tvec[0][0][0] = self.tvec[0][0][0]
                self.tvec[0][0][1] = -self.tvec[0][0][1]
                self.tvec[0][0][2] = -self.tvec[0][0][2]

                self.rvec[0][0][1] = -self.rvec[0][0][1]
                self.rvec[0][0][2] = -self.rvec[0][0][2]

                rot_m = self.constans.compositeArray(cv2.Rodrigues(self.rvec)[0], self.tvec[0][0])
                glPushMatrix()
                glLoadMatrixd(rot_m.T)
                glTranslate(self.x,self.y,self.z)
                game.castle.draw_model(self.own_model['castle'])
                for k in self.models_data:
                    if k != str(self.user_id):
                        self.direct.direct(self.models_data[k]['penguin'], self)
                    else:
                        self.direct.direct(self.own_model['penguin'], self)

                for l in self.models_data:
                    for m in self.models_data[l]['boxes']:
                        self.boxes[(self.models_data[l]['boxes'][m]['id']-1)].draw_model(self.models_data[l]['boxes'][m])

                glPushMatrix()
                glPushAttrib(GL_CURRENT_BIT)
                if(castle['fountain_right'] != True):
                    glTranslate(13,6,29)
                if(castle['fountain_left']!= True):
                    glTranslate(-13,6,29)
                glColor4f(0.0,1.0,1.0,1)
                glutSolidCube(6)
                glPopAttrib()
                glPopMatrix()
                glPopMatrix()
            glutPostRedisplay()
            glutSwapBuffers()
            self.requests.upload_world_changes(self.models_data)
        else:
            self.draw_over()

    def draw_over(self):
            if(self.was <3):
                self.was+=1
                glClearColor(0.8, 0.8, 1.0, 0.0)
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                bg =cv2.imread("images/win.jpg")
                self.background.draw(bg,self.dist, self.mtx,self.texture_background,[],[])
                glutPostRedisplay()
                glutSwapBuffers()
                glFlush()


    def keyboardF(self,key,x,y):
        if key == b'\x1b':
             sys.exit()

        self.keyboard.keyboardF(self.own_model['penguin'], self.penguins[self.user_id],game, key)

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
