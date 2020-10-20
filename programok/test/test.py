import numpy as np
import cv2
from calibration import *
from model import *

mtx, dist = load_coefficients("log.txt")



while(True):
        run, frame, rvec, tvec= track(mtx, dist)

        if run != False:
            drawn(rx, ry, tx, ty, zpos, rotate,  move, peng_x , peng_y ,peng_z , peng_rot_z,mtx, frame, rvec, tvec)
