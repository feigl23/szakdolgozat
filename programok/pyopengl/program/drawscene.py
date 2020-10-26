from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import cv2

from penguin import *
from box import *
from castle import *

class DrawScene:

    def __init__(self):
        self.castle = Castle()
        self.penguin = Penguin()
        self.box = Box()

    def init(self):
        self.castle.model.generate()
        self.penguin.model.generate()
        self.box.generate()

    def compositeArray(self, rvec, tvec):
        v = np.c_[rvec, tvec.T]
        v_ = np.r_[v, np.array([[0,0,0,1]])]
        return v_

    def view(self, mtx, rvec, tvec, ids):
        alpha = mtx[0][0]
        beta = mtx[1][1]
        cx = mtx[0][2]
        cy = mtx[1][2]
        f = 1000.0
        n = 1.0

        m1 = np.array([
            [(alpha)/cx, 0,       0,            0               ],
            [0,          beta/cy, 0,            0               ],
            [0,          0,       -(f+n)/(f-n), (-2.0*f*n)/(f-n)],
            [0,          0,       -1,           0               ],
        ])
        glLoadTransposeMatrixd(m1.T)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glPushMatrix()

        if not ids is None:
            tvec[0][0][0] = tvec[0][0][0]
            tvec[0][0][1] = -tvec[0][0][1]
            tvec[0][0][2] = -tvec[0][0][2]

            rvec[0][0][1] = -rvec[0][0][1]
            rvec[0][0][2] = -rvec[0][0][2]
            m = self.compositeArray(cv2.Rodrigues(rvec)[0], tvec[0][0])

            glLoadTransposeMatrixd(m.T)

            self.models()

        glPopMatrix()

    def models(self):
        self.penguin.drawn()
