from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import cv2
class DirectAnim:
    def direct(self, game):
        glEnable(GL_DEPTH_TEST)
        glDisable(GL_TEXTURE_2D)
        glLoadMatrixd(game.view)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        if not game.ids is None:
            game.tvec[0][0][0] = game.tvec[0][0][0]
            game.tvec[0][0][1] = -game.tvec[0][0][1]
            game.tvec[0][0][2] = -game.tvec[0][0][2]

            game.rvec[0][0][1] = -game.rvec[0][0][1]
            game.rvec[0][0][2] = -game.rvec[0][0][2]

            rot_m = game.constans.compositeArray(cv2.Rodrigues(game.rvec)[0], game.tvec[0][0])
            glPushMatrix()
            glLoadMatrixd(rot_m.T)
            glTranslate(game.x,game.y,game.z)

            game.castle.draw_model()
            game.box.draw_models()
            glPushMatrix()
            glPushAttrib(GL_CURRENT_BIT)
            if(game.box.right != True):
                glTranslate(13,6,28)
            if(game.box.left != True):
                glTranslate(-13,6,29)
            glColor4f(0.0,1.0,1.0,1)
            glutSolidCube(5.8)
            glPopAttrib()
            glPopMatrix()
            if(game.run_blue == True and game.run_lilac != True ):
                game.collision.collision(game.blue, game.lilac, game.box)
                game.blue.which_animation(game.i,game.box)
                game.lilac.draw_model()
                if(game.i ==game.blue.length-1):
                    game.anim = False
                    game.run_blue = False
                    game.is_not_end =False
                    game.blue.box =-1
                    game.blue.anim =""
            elif(game.run_lilac == True and game.run_blue != True ):
                game.collision.collision(game.lilac, game.blue, game.box)
                game.lilac.which_animation(game.i,game.box)
                game.blue.draw_model()
                if(game.i == game.lilac.length-1):
                    game.anim = False
                    game.run_lilac = False
                    game.is_not_end =False
                    game.lilac.box =-1
                    game.lilac.anim =""
            elif(game.run_blue == True and game.run_lilac == True):
                if(game.blue.anim == game.lilac.anim):
                    game.collision.collision(game.blue, game.lilac, game.box)
                    game.collision.collision(game.lilac, game.blue, game.box)
                    game.lilac.which_animation(game.i,game.box)
                    game.blue.which_animation(game.i,game.box)
                    if(game.i ==game.lilac.length-1):
                        game.is_not_end = game.run_blue = game.run_lilac =game.anim== False
                        game.blue.box =-1
                        game.lilac.box =-1
                        game.lilac.anim=""

                else:
                    if(game.blue.length>game.lilac.length):
                        if(game.blue<=game.lilac.length):
                            game.collision.collision(game.blue, game.lilac, game.box)
                            game.collision.collision(game.lilac, game.blue, game.box)
                            game.lilac.which_animation(game.i,game.box)
                            game.blue.which_animation(game.i,game.box)
                            if(game.i ==game.lilac.length-1):
                                game.run_lilac= False
                                game.lilac.box =-1
                                game.lilac.anim=""
                        else:
                            game.collision.collision(game.blue, game.lilac, game.box)
                            game.lilac.draw_model(i)
                            game.blue.which_animation(game.i,game.box)
                            if(game.i ==game.blue.length-1):
                                game.is_not_end = game.run_blue = game.anim= False
                                game.blue.box =-1
                                game.blue.anim=""
                    else:
                        if(game.blue.length>=game.lilac.length):
                            game.collision.collision(game.blue, game.lilac, game.box)
                            game.collision.collision(game.lilac, game.blue, game.box)
                            game.lilac.which_animation(game.i,game.box)
                            game.blue.which_animation(game.i,game.box)
                            if(game.i ==game.blue.length-1):
                                game.run_blue = False
                                game.blue.box =-1
                                game.blue.anim=""

                        else:
                            game.collision.collision(game.blue, game.lilac, game.box)
                            game.lilac.which_animation(game.i,game.box)
                            game.blue.draw_model(i)
                            if(game.i == game.lilac.length-1):
                                game.is_not_end =game.anim= game.run_lilac = False
                                game.lilac.box =-1
                                game.lilac.anim=""

            else:
                game.is_not_end = game.run_lilac= game.anim = game.run_blue =  False
                game.lilac.box =-1
                game.blue.box =-1
            glPopMatrix()
        game.i+=1
