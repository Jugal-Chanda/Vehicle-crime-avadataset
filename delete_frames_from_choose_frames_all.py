import os
import shutil

current_dir = os.getcwd()
choose_frames_all_dir = os.path.join(current_dir, "choose_frames_all")
choose_frames_dir = os.path.join(current_dir, "choose_frames")

all_dirs_of_choose_frames = os.listdir(choose_frames_dir)

all_files = os.listdir(choose_frames_all_dir)

for file in all_files:
    file_path = os.path.join(choose_frames_all_dir, file)

    temp_file_name = file.split('_')[0]
    if temp_file_name not in all_dirs_of_choose_frames:
        os.remove(file_path)
