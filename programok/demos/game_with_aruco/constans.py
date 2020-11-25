import cv2
import numpy as np

class Constans:

    def load_coefficients(self,path):
        cv_file = cv2.FileStorage(path, cv2.FILE_STORAGE_READ)
        camera_matrix = cv_file.getNode("CameraMatrix").mat()
        dist_matrix = cv_file.getNode("DistortionCoeff").mat()
        cv_file.release()
        return [camera_matrix, dist_matrix]

    def get_matrix(self):
        mtx,dist = self.load_coefficients("log.json")
        alpha =mtx[0][0]
        beta = mtx[1][1]
        cx = mtx[0][2]
        cy = mtx[1][2]
        f = 1000.0
        n = 1.0

        view = np.array([
        [(alpha)/cx, 0,       0,                0 ],
        [0,          beta/cy, 0,                0 ],
        [0,          0,       -(f+n)/(f-n),     -1],
        [0,          0,       (-2.0*f*n)/(f-n), 0 ],
        ])
        return view, mtx,dist

    def compositeArray(self,rvec, tvec):
        v = np.c_[rvec, tvec.T]
        v_ = np.r_[v, np.array([[0,0,0,1]])]
        return v_
