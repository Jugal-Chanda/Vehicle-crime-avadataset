import os
import shutil
import sys

current_dir = os.getcwd()
choose_frames_dir = os.path.join(current_dir, "choose_frames")
choose_frames_middle_dir = os.path.join(current_dir, "choose_frames_middle")
if not os.path.exists(choose_frames_middle_dir):
    os.mkdir(choose_frames_middle_dir)


for filepath, dirnames, filenames in os.walk(choose_frames_dir):
    if len(filenames) == 0:
        continue

    temp_name = filepath.split('/')[-1]
    path_temp_name = os.path.join(choose_frames_middle_dir, temp_name)
    if not os.path.exists(path_temp_name):
        os.makedirs(path_temp_name)
        print(path_temp_name)
    filenames = sorted(filenames)
    for filename in filenames:
        if "checkpoint" in filename:
            continue
        if "Store" in filename:
            continue
        temp_num = filename.split('_')[1]
        temp_num = temp_num.split('.')[0]
        temp_num = int(temp_num)

        if (temp_num)/30 <= 1 or (temp_num)/30 >= len(filenames) - 2:
            continue
        temp_num = str(temp_num)
        temp_num = temp_num.zfill(6)
        temp_num = temp_name + "_" + temp_num + ".jpg"

        srcfile = filepath + '/' + temp_num
        dstpath = os.path.join(path_temp_name, temp_num)
        shutil.copy(srcfile, dstpath)
