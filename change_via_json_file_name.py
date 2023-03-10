import os
import shutil

current_dir = os.getcwd()
choose_frames_middle_dir = os.path.join(current_dir, "choose_frames_middle")

all_frame_dirs = os.listdir(choose_frames_middle_dir)

new_json_file_template = "{}_finish.json"

for root, dirs, files in os.walk(choose_frames_middle_dir):
    for file in files:

        if ".json" in file:
            if "finish.json" in file:
                continue
            print(file, root)
            new_json_file = os.path.join(
                root, new_json_file_template.format(str(os.path.basename(root))))
            shutil.copy(os.path.join(
                        root, file), new_json_file)
