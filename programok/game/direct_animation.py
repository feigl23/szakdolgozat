from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class DirectAnim:
    def direct(self, game):
        i = 1
        while(game.is_end):
            glClearColor(0.8, 0.8, 1.0, 0.0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            glTranslate(game.x,game.y,game.z)
            game.castle.draw_model()
            game.box.draw_models()
            if(game.run_blue == True and game.run_lilac != True ):

                game.collision.collision(game.blue, game.lilac, game.box)
                game.blue.which_animation(i)
                game.lilac.draw_model()
                if(i ==game.blue.length-1):
                    game.run_blue = False
                    game.is_end =False
            elif(game.run_lilac == True and game.run_blue != True ):

                game.collision.collision(game.lilac, game.blue, game.box)
                game.lilac.which_animation(i)
                game.blue.draw_model()
                if(i == game.lilac.length-1):
                    game.run_lilac = False
                    game.is_end =False
            elif(game.run_blue == True and game.run_lilac == True):
                if(game.blue.anim == game.lilac.anim):
                    game.collision.collision(game.blue, game.lilac, game.box)
                    game.collision.collision(game.lilac, game.blue, game.box)
                    game.lilac.which_animation(i)
                    game.blue.which_animation(i)
                    if(i ==game.lilac.length-1):
                        game.is_end = game.run_blue = game.run_lilac = False
                else:
                    if(game.blue.length>game.lilac.length):
                        if(game.blue<=game.lilac.length):
                            game.collision.collision(game.blue, game.lilac, game.box)
                            game.collision.collision(game.lilac, game.blue, game.box)
                            game.lilac.which_animation(i)
                            game.blue.which_animation(i)
                        else:
                            game.collision.collision(game.blue, game.lilac, game.box)
                            game.lilac.draw_model(i)
                            game.blue.which_animation(i)
                            if(i ==game.blue.length-1):
                                game.is_end = game.run_blue = game.run_lilac = False
                    else:
                        if(game.blue>=game.lilac.length):
                            game.collision.collision(game.blue, game.lilac, game.box)
                            game.collision.collision(game.lilac, game.blue, game.box)
                            game.lilac.which_animation(i)
                            game.blue.which_animation(i)
                        else:
                            game.collision.collision(game.blue, game.lilac, game.box)
                            game.lilac.which_animation(i)
                            game.blue.draw_model(i)
                            if(i == game.lilac.length-1):
                                game.is_end = game.run_blue = game.run_lilac = False
            else:
                break
            glutPostRedisplay()
            glutSwapBuffers()
            i+=1
        return False
