import os
from pytube import YouTube

SAVE_PATH = "downloaded_videos"
approved_video_ids_filename = "approved_video_ids.txt"

downloaded_video_ids_filename = "downloaded_video_ids.txt"

approved_video_file = open(approved_video_ids_filename)

video_ids = approved_video_file.readlines()
approved_video_file.close()

video_ids = [x.strip() for x in video_ids]

downloaded_ids = []


cnt = 0
for video_id in video_ids:
    if cnt == 5:
        break
    link = "https://www.youtube.com/watch?v="+video_id
    try:
        yt = YouTube(link)
    except:
        print("Connection Error")  # to handle exception

    yt = yt.streams.get_highest_resolution()
    try:
        filename = video_id+".mp4"
        # yt.download(SAVE_PATH, filename=filename)
        print(video_id, "Downloded")
        video_ids.remove(video_id)
        downloaded_ids.append(video_id)
        with open(approved_video_ids_filename, "w") as f:
            f.write("\n".join(video_ids))
        with open(downloaded_video_ids_filename, "w") as f:
            f.write("\n".join(downloaded_ids))
        cnt += 1
    except Exception as exp:
        print(exp)
