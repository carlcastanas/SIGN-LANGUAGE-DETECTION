import copy
import itertools
# import logging
def pre_process_landmark(landmark_list):
    temp_landmark_list = copy.deepcopy(landmark_list)
#  print(temp_landmark_list)
    base_x, base_y = 0, 0
    for index, landmark_point in enumerate(temp_landmark_list):
        if index == 0:
            base_x, base_y = landmark_point[0], landmark_point[1]
#     print(base_x,base_y)
        temp_landmark_list[index][0] = temp_landmark_list[index][0] - base_x
        temp_landmark_list[index][1] = temp_landmark_list[index][1] - base_y
#    print(temp_landmark_list)
    temp_landmark_list = list(
        itertools.chain.from_iterable(temp_landmark_list))
# print(temp_landmark_list)
    max_value = max(list(map(abs, temp_landmark_list)))
# print(max_value)
    def normalize_(n):
        return n / max_value
# print(normalize_(max_value))
    temp_landmark_list = list(map(normalize_, temp_landmark_list))

    return temp_landmark_list