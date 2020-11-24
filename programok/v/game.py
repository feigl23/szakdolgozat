
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
from timer import *
import cv2
import time


cap = cv2.VideoCapture(0)

class Game:
    def __init__(self):
        self.user_id= 0
        self.castle = Castle()
        self.penguins = []
        self.boxes = []
        self.max = 2
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
        self.timer = Timer()
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
        self.fountain={"left": True,"right": False}
        self.models_data = { 'penguins':[{
            "id" :self.user_id,
            "position":(0,3.2,5.5),
            "rot_z" : 180,
            "axis" : "y",
            "anim" : "",
            "color" : [1,0,1],
            "length":0,
            "box" :-1,
            "box_axis" : "" ,
            "anim_i":0
            }],
            'boxes':[
            {
            "id" :1,
            "color" : [1,0,1],
            "position" : (-14,13,30),
            },
            {
            "id" :2,
            "color" : [1,0,1],
            "position" : (-14,-2,30),
            },
            { "id" :3,
            "color" : [1,0,1],
            "position" : (-10,-2,30),
            },
            {
            "id" :4,
            "color" : [1,0,1],
            "position" : (-10,13,30),
            }],
            'castle':{
                "position" : (0,0,-30),
            }}

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


    def capture(self):
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
            game.castle.draw_model(self.models_data['castle'])
            for model_d in self.models_data['penguins']:
                self.direct.direct(model_d, self)

            for box in self.models_data['boxes']:
                self.boxes[box['id']-1].draw_model(box)

            glPushMatrix()
            glPushAttrib(GL_CURRENT_BIT)
            if(self.fountain['right'] != True):
                glTranslate(13,6,29)
            if(self.fountain['left'] != True):
                glTranslate(-13,6,29)
            glColor4f(0.0,1.0,1.0,1)
            glutSolidCube(6)
            glPopAttrib()
            glPopMatrix()
            glPopMatrix()
        glutPostRedisplay()
        glutSwapBuffers()

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


    def keyboardF(self,key,x,y):
        if key == b'\x1b':
             sys.exit()
        print(self.models_data['penguins'][self.user_id], self.penguins[self.user_id])
        #self.keyboard.keyboardF(self.models_data['penguins'][self.user_id], self.penguins[self.user_id], key)

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
