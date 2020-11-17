import cv2.aruco as aruco
import numpy as np
import cv2
from PIL import Image


def save_data(rvec, tvec, path):

    cv_file = cv2.FileStorage(path, cv2.FILE_STORAGE_WRITE)
    cv_file.write("RVEC", rvec)
    cv_file.write("TVEC", tvec)

    cv_file.release()

def load_coefficients(path):

    cv_file = cv2.FileStorage(path, cv2.FILE_STORAGE_READ)

    camera_matrix = cv_file.getNode("CameraMatrix").mat()
    dist_matrix = cv_file.getNode("DistortionCoeff").mat()

    cv_file.release()
    return [camera_matrix, dist_matrix]

def find_aruco(path, mtx, dist, target_path):
    frame = cv2.imread(path)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_100)
    parameters = aruco.DetectorParameters_create()
    parameters.adaptiveThreshConstant = 10
    corners, ids, rejectedImgPoints = aruco.detectMarkers(image, aruco_dict,
                                                        parameters=parameters,
                                                        cameraMatrix=mtx,
                                                        distCoeff=dist)


    if np.all(ids is not None):
        for i in range(0, len(ids)):
            aruco.drawDetectedMarkers(frame, corners)
            rvec, tvec ,_ = aruco.estimatePoseSingleMarkers(corners, 0.017, mtx, dist)
            aruco.drawAxis(frame, mtx, dist, rvec, tvec, 0.017)
            cv2.imwrite(target_path, frame)

        return rvec, tvec
    else:
        cv2.imwrite(target_path, frame)
        return 0,0


mtx, dist = load_coefficients("log.json")

for i in range(1,13):
    path = "images/" +str(i)+".jpg"
    target_path =  "results/"+str(i)+".jpg"
    rvec, tvec = find_aruco(path,mtx,dist,target_path)
    print(str(i), ". tvec:" ,tvec , ",\nrvec:", rvec)
    target_path_log =  "results/"+str(i)+".json"
    save_data(rvec, tvec, target_path_log)
