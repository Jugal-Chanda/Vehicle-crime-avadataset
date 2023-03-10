import shutil
import os

current_dir = os.getcwd()
choose_frames_middle_dir = os.path.join(current_dir, "choose_frames_middle")

all_frame_dirs = os.listdir(choose_frames_middle_dir)

new_json_file_template = "{}_finish.json"

need_to_delete = []

for frame_dir in all_frame_dirs:
    frame_dir_path = os.path.join(choose_frames_middle_dir, frame_dir)

    all_files = os.listdir(frame_dir_path)

    need_to_delete_this = True
    for file in all_files:
        if "finish.json" in file:
            need_to_delete_this = False
    if need_to_delete_this:
        need_to_delete.append(frame_dir_path)


for dir in need_to_delete:
    shutil.rmtree(dir)
