import cv2
import os
from pytube import YouTube
import json
import math

current_dir = os.getcwd()
frames_dir = os.path.join(current_dir, "extracted_frames")
video_download_dir = os.path.join(current_dir, "videos")


if not os.path.exists(frames_dir):
    print("extracted_frames dir not found creating it")
    os.mkdir(frames_dir)

if not os.path.exists(video_download_dir):
    print("videos dir not found creating it")
    os.mkdir(video_download_dir)

with open("final_video_ids_with_time.json") as f:
    video_ids = json.load(f)

with open("extracted_frames_video_ids.json") as f:
    downloaded_video_ids = json.load(f)

cnt = 0
for video_id in video_ids.keys():
    if video_id in downloaded_video_ids:
        continue
    if cnt == 1:
        break
    link = "https://www.youtube.com/watch?v="+video_id
    try:
        yt = YouTube(link)
    except:
        print("Connection Error")  # to handle exception

    yt = yt.streams.get_highest_resolution()
    video_downloaded = False
    try:
        filename = video_id+".mp4"
        yt.download(video_download_dir, filename=filename)
        print(video_id, "Downloded")
        # del video_ids[video_id]
        downloaded_video_ids.append(video_id)
        cnt += 1
        video_downloaded = True

    except Exception as exp:
        print(exp)

    times = video_ids[video_id]

    if video_downloaded:

        video_path = os.path.join(video_download_dir, filename)
        len_frames_dir = len(os.listdir(frames_dir))

        for time in times:
            len_frames_dir += 1
            tmp_frame_dir = os.path.join(frames_dir, str(len_frames_dir))

            if not os.path.exists(tmp_frame_dir):
                os.mkdir(tmp_frame_dir)

            vcap = cv2.VideoCapture(video_path)
            fps = vcap.get(cv2.CAP_PROP_FPS)
            fps = 30
            start_time, end_time = time
            start_minute, start_second = math.floor(
                start_time), ((start_time*100) % 100)
            end_minute, end_second = math.floor(
                end_time), ((end_time*100) % 100)

            start_second = (start_minute*60)+start_second
            end_second = (end_minute*60)+end_second

            start_frame = int(start_second*fps)
            end_frame = int(end_second*fps)

            while True:
                ret, frame = vcap.read()
                if ret:
                    current_frame_number = int(
                        vcap.get(cv2.CAP_PROP_POS_FRAMES))
                    print(current_frame_number)
                    if current_frame_number >= start_frame and current_frame_number <= end_frame:
                        frame_path = os.path.join(
                            tmp_frame_dir, str(current_frame_number)+".jpg")
                        cv2.imwrite(frame_path, frame)
                    elif current_frame_number > end_frame:
                        break
                else:
                    break

            vcap.release()

with open("final_video_ids_with_time.json", "w") as f:
    json.dump(video_ids, f)

with open("extracted_frames_video_ids.json", "w") as f:
    json.dump(downloaded_video_ids, f)
