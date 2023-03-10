import os
import shutil

current_dir = os.getcwd()
choose_frames_all_dir = os.path.join(current_dir, "choose_frames_all")

temp_choose_frames_all_dir = os.path.join(
    current_dir, "temp_choose_frames_all")
if not os.path.exists(temp_choose_frames_all_dir):
    os.mkdir(temp_choose_frames_all_dir)

filename_template = "{}_{}.jpg"

all_files = os.listdir(choose_frames_all_dir)
all_files = sorted(all_files, key=lambda x: int(x.split('_')[0]))
previous_frame_dir_num = int(all_files[0].split('_')[0])

for i, file in enumerate(all_files):
    file_path = os.path.join(choose_frames_all_dir, file)
    current_frame_dir_num = int(file.split('_')[0])
    frame_number = file.split('_')[1].split('.')[0]
    if current_frame_dir_num == previous_frame_dir_num:
        continue
    elif (previous_frame_dir_num+1) == current_frame_dir_num:
        previous_frame_dir_num = current_frame_dir_num
        continue
    else:
        new_filename = filename_template.format(
            str(previous_frame_dir_num + 1), frame_number)
        new_file_path = os.path.join(choose_frames_all_dir, new_filename)
        shutil.move(file_path, new_file_path)
        next_frame_dir_num = (current_frame_dir_num + 1) if (i ==
                                                             (len(all_files) - 1)) else int(all_files[i+1].split('_')[0])
        if next_frame_dir_num > current_frame_dir_num:
            previous_frame_dir_num = previous_frame_dir_num + 1
