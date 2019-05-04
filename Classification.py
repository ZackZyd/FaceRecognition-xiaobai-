import numpy as np
import os
from os import listdir
import glob as gb
import cv2

path_img = r'./datasets/faces-data/*.jpg'
img_path = gb.glob(path_img)

save_path_test = "./datasets/test/"
save_path_train = "./datasets/train/"

# datasetList = listdir("./datasets/")
# temp = 0
# count = 0
# count_test = 0
# count_train = 0
# count_class = 0
Happened = []
Frequency = []
class_name = 0
# for i in rage(3059)
for path in img_path:
    img = cv2.imread(path)
    filename = path
    file_whole = filename.split('\\')[1]
    file_part = file_whole.split('.')[0]

    if file_part in Happened:
        if Frequency[Happened.index(file_part)] <= 2:
            savepath = os.path.join(save_path_test+str(Happened.index(file_part)), str(Happened.index(file_part)))
            cv2.imwrite(savepath + file_whole, img)
            Frequency[Happened.index(file_part)] += 1
        elif Frequency[Happened.index(file_part)] > 2:
            # mkpath = save_path_train + str(Happened.index(file_part))
            # os.mkdir(mkpath)
            savepath = os.path.join(save_path_train+str(Happened.index(file_part)), str(Happened.index(file_part)))
            cv2.imwrite(savepath + file_whole, img)
            Frequency[Happened.index(file_part)] += 1

    else:
        Happened.append(file_part)
        Frequency.append(1)
        mkpath = save_path_test+str(Happened.index(file_part))
        os.mkdir(mkpath)
        savepath = os.path.join(mkpath, str(Happened.index(file_part)))
        cv2.imwrite(savepath+file_whole, img)
        mkpath = save_path_train + str(Happened.index(file_part))
        os.mkdir(mkpath)
# if file != temp and count < 2:
#     temp = file
#     count += 1
#     savepath = os.path.join(save_path_test, str(count_test))

#     cv2.imwrite(savepath, img)
#     count_class += 1
# elif file == temp and count < 2:
#     temp = file
#     count += 1
#     savepath = os.path.join(save_path_1, count_test)
#     cv2.imwrite(savepath, file)
#     count_test = 0
# elif file == temp and count >= 2:
#     temp = file
#     count += 1
#     savepath = os.path.join(save_path_1, count_train)
#     cv2.imwrite(savepath, file)
# elif file != temp and count >= 2:
#     count = 0
#     temp = file
#     savepath = os.path.join(save_path_1, count_test)
#     cv2.imwrite(savepath, file)
#     count_class += 1
#
#
