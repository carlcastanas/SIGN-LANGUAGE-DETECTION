import numpy as np
import cv2 as cv
# from app_files import calc_landmark_list, draw_landmarks, get_args, pre_process_landmark,logging_csv
def calc_landmark_list(image, landmarks):
    image_width, image_height = image.shape[1], image.shape[0]
#   print(image_width,image_height)
    landmark_point = []
#  print(landmarks)
    for _, landmark in enumerate(landmarks.landmark):
        landmark_x = min(int(landmark.x * image_width), image_width - 1)
        landmark_y = min(int(landmark.y * image_height), image_height - 1)
        landmark_point.append([landmark_x, landmark_y])
   
    return landmark_point
