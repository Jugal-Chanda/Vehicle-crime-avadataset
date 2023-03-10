import os
import shutil
import json
import copy

current_dir = os.getcwd()
choose_frames_middle_dir = os.path.join(current_dir, "choose_frames_middle")

filename_template = "{}_{}.jpg"
json_file_format = "{}_finish.json"


all_frame_dirs = os.listdir(choose_frames_middle_dir)
all_frame_dirs = sorted(all_frame_dirs, key=lambda x: int(x))

for i, frame_dir in enumerate(all_frame_dirs):
    frame_dir_path = os.path.join(choose_frames_middle_dir, frame_dir)

    all_files = os.listdir(frame_dir_path)

    for file in all_files:
        file_path = os.path.join(frame_dir_path, file)
        if "_finish.json" not in file:
            continue
        json_file_dir_num = file.split('_')[0]
        if json_file_dir_num == frame_dir:
            continue

        with open(file_path) as json_file:
            json_data = json.load(json_file)
        files_data = copy.deepcopy(json_data['file'])
        for file_data in files_data:
            data = files_data[file_data]
            filename = data['fname']
            filename_num = filename.split('_')[1].split('.')[0]
            new_file_name = filename_template.format(frame_dir, filename_num)
            data['fname'] = new_file_name
            files_data[file_data] = data
        json_data['file'] = files_data
        new_json_file_name = json_file_format.format(frame_dir)
        new_json_file_path = os.path.join(frame_dir_path, new_json_file_name)
        with open(new_json_file_path, 'w') as outfile:
            json.dump(json_data, outfile)
