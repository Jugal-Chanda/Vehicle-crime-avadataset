import sys
import os
import json
import pickle
import torch
import cv2

current_dir = os.getcwd()
choose_frames_all_dir = os.path.join(current_dir, "choose_frames_all")
model = torch.hub.load('WongKinYiu/yolov7', 'custom', 'yolov7.pt',
                       force_reload=True, trust_repo=True)


avaMin_dense_proposals_path = os.path.join(
    current_dir, "dense_proposal_train.pkl")

results_dict = {}
dicts = []

for root, dirs, files in os.walk(choose_frames_all_dir):
    lenFile = len(files)/3
    files.sort(key=lambda arr: (int(arr[:-7]), int(arr[3:-4])))
    for name in files:
        temp_file_name = name.split("_")[0]
        temp_video_ID = name.split("_")[1].split('.')[0]
        temp_video_ID = int(temp_video_ID)
        temp_video_ID = str(int((temp_video_ID-1)/30))
        temp_video_ID = temp_video_ID.zfill(4)

        if int(temp_video_ID) <= 1 or int(temp_video_ID) >= lenFile:
            continue

        key = temp_file_name + ',' + temp_video_ID
        frame_path = os.path.join(root, name)
        frame = cv2.imread(frame_path)
        model_results = model(frame)
        model_results.pandas().xyxy[0]
        objects = model_results.pandas().xyxy[0].to_json(orient="records")
        objects = json.loads(objects)
        results = []

        for object in objects:
            parsed = object
            # if parsed['confidence'] > gun_model.conf:
            if parsed['name'] == 'car' or parsed['name'] == 'person':
                top = int(parsed['ymin'])
                right = int(parsed['xmax'])
                bottom = int(parsed['ymax'])
                left = int(parsed['xmin'])
                results.append(
                    [left, top, right, bottom, parsed['confidence']])
                dicts.append([left, top, right, bottom, parsed['confidence']])
        results_dict[key] = results
with open(avaMin_dense_proposals_path, "wb") as pklfile:
    pickle.dump(results_dict, pklfile)

for i in results_dict:
    print(i, results_dict[i])
