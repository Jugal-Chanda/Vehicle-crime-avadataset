import os
import shutil
import sys

current_dir = os.getcwd()
renamed_frames_dir = os.path.join(current_dir, "renamed_frames")
choose_frames_all_dir = os.path.join(current_dir, "choose_frames_all")

if not os.path.exists(choose_frames_all_dir):
    os.mkdir(choose_frames_all_dir)

seconds = 10
start = 0

frames = range(start, seconds+1)

num_frames = []

for i in frames:
    num_frames.append(i*30)

for filepath, dirnames, filenames in os.walk(renamed_frames_dir):
    filenames = sorted(filenames)
    temp_name = filepath.split('/')[-1]
    for filename in filenames:
        if "checkpoint" in filename:
            continue
        if "Store" in filename:
            continue
        temp_num = filename.split('_')[1]
        temp_num = temp_num.split('.')[0]
        temp_num = int(temp_num)
        if temp_num in num_frames:
            temp_num = str(temp_num)
            temp_num = temp_num.zfill(6)
            temp_num = temp_name + "_" + temp_num + ".jpg"

            srcfile = os.path.join(filepath, temp_num)
            dstpath = os.path.join(choose_frames_all_dir, temp_num)
            shutil.copy(srcfile, dstpath)
