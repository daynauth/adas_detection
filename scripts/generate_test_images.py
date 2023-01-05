"""
@author: Roland Daynauth
@date: 12-07-2022
@description: This script generates test images for the model
"""

import cv2
#import matplotlib.pyplot as plt

def generate_test_images():
    """
    This function generates test images for the model
    """
    path = 'RoadData_2020_03_09_150631_c3_001_out.avi'
    #read avi video
    cam = cv2.VideoCapture(path, cv2.CAP_OPENCV_MJPEG)

    # length = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
    # print( length )

    if cam.isOpened():
        ret, frame = cam.read()  # read first frame
        cv2.imwrite("test.png", frame)

        cam.release()
    else:
        print("cannot open video file")

    #cv2.destroyAllWindows()

if __name__ == "__main__":
    generate_test_images()