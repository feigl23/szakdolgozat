from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class DirectAnim:
    def direct(self, game):
        i = 1
        while(game.is_not_end):
            glClearColor(0.8, 0.8, 1.0, 0.0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            glTranslate(game.x,game.y,game.z)
            game.castle.draw_model()
            game.box.draw_models()
            if(game.run_blue == True and game.run_lilac != True ):
                game.collision.collision(game.blue, game.lilac, game.box)
                game.blue.which_animation(i,game.box)
                game.lilac.draw_model()
                if(i ==game.blue.length-1):
                    game.run_blue = False
                    game.is_not_end =False
                    game.blue.box =-1
            elif(game.run_lilac == True and game.run_blue != True ):
                game.collision.collision(game.lilac, game.blue, game.box)
                game.lilac.which_animation(i,game.box)
                game.blue.draw_model()
                if(i == game.lilac.length-1):
                    game.run_lilac = False
                    game.is_not_end =False
                    game.lilac.box =-1
            elif(game.run_blue == True and game.run_lilac == True):
                if(game.blue.anim == game.lilac.anim):
                    game.collision.collision(game.blue, game.lilac, game.box)
                    game.collision.collision(game.lilac, game.blue, game.box)
                    game.lilac.which_animation(i,game.box)
                    game.blue.which_animation(i,game.box)
                    if(i ==game.lilac.length-1):
                        game.is_not_end = game.run_blue = game.run_lilac = False
                        game.blue.box =-1
                        game.lilac.box =-1
                else:
                    if(game.blue.length>game.lilac.length):
                        if(game.blue<=game.lilac.length):
                            game.collision.collision(game.blue, game.lilac, game.box)
                            game.collision.collision(game.lilac, game.blue, game.box)
                            game.lilac.which_animation(i,game.box)
                            game.blue.which_animation(i,game.box)
                            if(i ==game.lilac.length-1):
                                game.run_lilac = False
                                game.lilac.box =-1
                        else:
                            game.collision.collision(game.blue, game.lilac, game.box)
                            game.lilac.draw_model(i)
                            game.blue.which_animation(i,game.box)
                            if(i ==game.blue.length-1):
                                game.is_not_end = game.run_blue = False
                                game.blue.box =-1
                    else:
                        if(game.blue.length>=game.lilac.length):
                            game.collision.collision(game.blue, game.lilac, game.box)
                            game.collision.collision(game.lilac, game.blue, game.box)
                            game.lilac.which_animation(i,game.box)
                            game.blue.which_animation(i,game.box)
                            if(i ==game.blue.length-1):
                                game.run_blue = False
                                game.blue.box =-1
                        else:
                            game.collision.collision(game.blue, game.lilac, game.box)
                            game.lilac.which_animation(i,game.box)
                            game.blue.draw_model(i)
                            if(i == game.lilac.length-1):
                                game.is_not_end = game.run_lilac = False
                                game.lilac.box =-1
            else:
                break
            glutPostRedisplay()
            glutSwapBuffers()
            i+=1
        return False
