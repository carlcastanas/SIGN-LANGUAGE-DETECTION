import csv
# from app_files import calc_landmark_list, draw_landmarks, get_args, pre_process_landmark,logging_csv
def logging_csv(number, mode, landmark_list):
    if mode == 1 and (0 <= number <= 9):
        csv_path = 'model/keypoint_classifier/keypoint.csv'
        with open(csv_path, 'a', newline="") as f:
            writer = csv.writer(f)
            writer.writerow([number, *landmark_list])
    return