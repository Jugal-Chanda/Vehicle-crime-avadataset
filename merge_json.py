import json

json_file_1 = open("extract_frame_1.json")
json_data_1 = json.load(json_file_1)

json_file_2 = open("extract_frame_2.json")
json_data_2 = json.load(json_file_2)

json_data_1.update(json_data_2)
print(json_data_1)
print(len(json_data_1.keys()))

with open("final_video_ids_with_time.json", "w") as f:
    json.dump(json_data_1,f)
