import os
import shutil

current_dir = os.getcwd()
choose_frames_middle_dir = os.path.join(current_dir, "choose_frames_middle")
choose_frames_dir = os.path.join(current_dir, "choose_frames")

all_dirs_of_choose_frames_middle = os.listdir(choose_frames_middle_dir)
all_dirs_of_choose_frames = os.listdir(choose_frames_dir)

for dir in all_dirs_of_choose_frames:
    dir_path = os.path.join(choose_frames_dir, dir)
    if dir not in all_dirs_of_choose_frames_middle:
        shutil.rmtree(dir_path)
