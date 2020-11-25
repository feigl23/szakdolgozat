from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

width = 500
height= 500
x = 450
y = 150
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(x, y)
    glutCreateWindow("pyonpengl window")
    glutMainLoop()
main()
