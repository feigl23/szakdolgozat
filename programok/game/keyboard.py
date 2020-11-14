from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Keyboard:
    def keyboardF(self,game,key):
        if key == b'\x1b':
          sys.exit()
        elif key == b'a':
                game.blue.rot_z +=90
        elif key == b'w':
            if(game.run_blue != True):
                game.run_blue = True
                game.anim = True
                game.blue.anim = "walk"
                game.blue.length = 31
                if game.blue.rot_z == 90 or game.blue.rot_z ==-270 :
                    game.blue.axis = "x"
                    game.blue.dist =-1*game.blue.const_dist
                elif game.blue.rot_z == 180 or game.blue.rot_z == -180:
                    game.blue.axis = "y"
                    game.blue.dist =-1*game.blue.const_dist
                elif game.blue.rot_z == 270 or game.blue.rot_z == -90:
                    game.blue.axis = "x"
                    game.blue.dist =game.blue.const_dist
                else:
                    game.blue.axis = "y"
                    game.blue.dist =game.blue.const_dist

        elif key == b's':
            if(game.run_blue != True):
                game.run_blue= True
                game.blue.anim="walk"
                game.anim = True
                game.blue.length = 31
                if  game.blue.rot_z == -90 or game.blue.rot_z == 270:
                    game.blue.axis = "x"
                    game.blue.dist =-1*game.blue.const_dist
                elif  game.blue.rot_z == 180 or game.blue.rot_z == -180:
                    game.blue.axis = "y"
                    game.blue.dist =game.blue.const_dist
                elif  game.blue.rot_z == -270 or game.blue.rot_z == 90:
                    game.blue.axis = 'x'
                    game.blue.dist =game.blue.const_dist
                else:
                    game.blue.axis = 'y'
                    game.blue.dist =-1*game.blue.const_dist

        elif key ==  b'd':
                game.blue.rot_z -=90
        #elif key == b' ':
        #    if(game.run_blue != True):
        #        game.run_blue = True
        #        game.anim = True
        #        game.blue.anim="jump"
        #        game.tav = (0.5/30)
        #        game.blue.axis ="z"
        #        game.blue.length=21
        #elif key == b'i':
        #    if(game.run_lilac != True):
        #        game.run_lilac = True
        #        game.anim = True
        ##        game.lilac.anim="jump"
        #        game.tav = (0.5/30)
        #        game.lilac.axis ="z"
        #        game.lilac.length=21
        #elif key == b'k':
        #    if(game.run_lilac != True):
        #        game.run_lilac = True
        #        game.anim = True
        #        game.lilac.anim="grab"
        #        game.tav = (0.5/30)
        #        game.lilac.axis ="z"
        #        game.lilac.length=16
        #elif key == b'l':
        #    if(game.run_lilac != True):
        #        game.run_lilac = True
        #        game.anim = True
        #        game.lilac.anim="release"
        #        game.tav = (0.5/30)
        #        game.lilac.axis ="z"
        #        game.lilac.length=16
        #elif key == b'e':
        #    if(game.run_blue != True):
        #        game.run_blue = True
        #        game.anim = True
        #        game.blue.anim="grab"
        #        game.blue.length=16
        #elif key == b'r':
        #    if(game.run_blue != True):
        #        game.run_blue = True
        #        game.anim = True
        #        game.blue.anim="release"
        #        game.blue.length=16



        if(game.blue.rot_z==360 or game.blue.rot_z ==-360):
            game.blue.rot_z = 0

    def arrows(self,game,key):
        if key == GLUT_KEY_LEFT:
                game.lilac.rot_z +=90
        elif key == GLUT_KEY_UP:
            if(game.run_lilac != True):
                game.run_lilac= True
                game.anim = True
                game.lilac.anim="walk"
                game.lilac.length = 31
                if game.lilac.rot_z == 90 or game.lilac.rot_z == -270:
                    game.lilac.axis="x"
                    game.lilac.dist=-1* game.lilac.const_dist
                elif game.lilac.rot_z == 180:
                    game.lilac.axis="y"
                    game.lilac.dist=-1*game.lilac.const_dist
                elif game.lilac.rot_z ==-180:
                    game.lilac.axis="y"
                    game.lilac.dist=-1*game.lilac.const_dist
                elif game.lilac.rot_z == 270 or game.lilac.rot_z == -90:
                    game.lilac.axis="x"
                    game.lilac.dist=game.lilac.const_dist
                else:
                    game.lilac.axis="y"
                    game.lilac.dist=game.lilac.const_dist

        elif key == GLUT_KEY_DOWN:
            if(game.run_lilac != True):
                game.run_lilac = True
                game.anim = True
                game.anim_name="walk"
                game.lilac.length = 31
                if  game.lilac.rot_z == -90 or game.lilac.rot_z == 270:
                    game.lilac.axis="x"
                    game.lilac.dist=-1*game.lilac.const_dist
                elif  game.lilac.rot_z == 180 :
                    game.lilac.axis="y"
                    game.lilac.dist=game.lilac.const_dist
                elif game.lilac.rot_z == -180 :
                    game.lilac.axis="y"
                    game.lilac.dist=game.lilac.const_dist
                elif  game.lilac.rot_z == -270 or game.lilac.rot_z == 90:
                    game.lilac.axis="x"
                    game.lilac.dist=game.lilac.const_dist
                else:
                    game.lilac.axis="y"
                    game.lilac.dist=-1*game.lilac.const_dist
        elif key == GLUT_KEY_RIGHT:
                game.lilac.rot_z -=90

        if(game.lilac.rot_z==360 or game.lilac.rot_z ==-360):
            game.lilac.rot_z = 0
