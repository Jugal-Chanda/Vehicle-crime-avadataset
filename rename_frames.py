import os
import shutil

current_dir = os.getcwd()
extracted_frames_dir = os.path.join(current_dir, "extracted_frames")
renamed_frames_dir = os.path.join(current_dir, "renamed_frames")

if not os.path.exists(renamed_frames_dir):
    os.mkdir(renamed_frames_dir)

frames_dirs = os.listdir(extracted_frames_dir)

for frame_dir in frames_dirs:
    frame_dir_path = os.path.join(extracted_frames_dir, frame_dir)
    all_frames = os.listdir(frame_dir_path)
    if len(all_frames) < 300:
        shutil.rmtree(frame_dir_path)
        continue
    new_frame_dir = os.path.join(renamed_frames_dir, str(
        len(os.listdir(renamed_frames_dir)) + 1))
    os.mkdir(new_frame_dir)
    for frame_name in all_frames:
        frame_path = os.path.join(frame_dir_path, frame_name)
        new_frame_name = str(len(os.listdir(new_frame_dir)))
        new_frame_name = frame_dir+"_"+new_frame_name.zfill(6)+".jpg"

        new_frame_path = os.path.join(new_frame_dir, new_frame_name)
        shutil.copy(frame_path, new_frame_path)
    shutil.rmtree(frame_dir_path)
