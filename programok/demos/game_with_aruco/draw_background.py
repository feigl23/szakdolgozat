from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import cv2
import cv2.aruco as aruco

class Background:

        def draw(self,frame, dist, mtx, texture_background, rvec, tvec):
            image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            heightI, widthI = image.shape[:2]
            if(rvec != []):
                aruco.drawAxis(image, mtx, dist, rvec, tvec, 7)
            glBindTexture(GL_TEXTURE_2D, texture_background)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, widthI, heightI, 0, GL_RGB, GL_UNSIGNED_BYTE, image)

            glBindTexture(GL_TEXTURE_2D, texture_background)
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
            glDisable(GL_TEXTURE_2D)
