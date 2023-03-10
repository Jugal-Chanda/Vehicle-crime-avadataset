import os
import shutil

current_dir = os.getcwd()
renamed_frames_dir = os.path.join(current_dir, "renamed_frames")


filename_template = "{}_{}.jpg"

all_frame_dirs = os.listdir(renamed_frames_dir)
all_frame_dirs = sorted(all_frame_dirs, key=lambda x: int(x))
previous_dir_num = 0


for i, frame_dir in enumerate(all_frame_dirs):
    frame_dir_path = os.path.join(renamed_frames_dir, frame_dir)

    current_dir_num = int(frame_dir)
    print(current_dir_num, previous_dir_num)

    if (previous_dir_num+1) == current_dir_num:
        previous_dir_num = current_dir_num
        continue
    else:
        all_files = os.listdir(frame_dir_path)
        new_frame_dir = previous_dir_num + 1
        new_frame_dir_path = os.path.join(
            renamed_frames_dir, str(new_frame_dir))
        if not os.path.exists(new_frame_dir_path):
            os.mkdir(new_frame_dir_path)
        print("move from {} to {}".format(frame_dir, new_frame_dir))

        for file in all_files:
            file_path = os.path.join(frame_dir_path, file)
            frame_number = file.split('_')[1].split('.')[0]

            new_filename = filename_template.format(
                str(new_frame_dir), frame_number)
            new_file_path = os.path.join(
                new_frame_dir_path, new_filename)
            shutil.move(file_path, new_file_path)
        print("deleting {}".format(frame_dir))
        shutil.rmtree(frame_dir_path)
        next_dir_num = (current_dir_num + 1) if (i ==
                                                 (len(all_frame_dirs) - 1)) else int(all_frame_dirs[i+1])
        if next_dir_num > current_dir_num:
            previous_dir_num = previous_dir_num + 1
