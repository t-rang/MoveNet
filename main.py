from dataset_model import Dataset

ur_path = "/Users/mac/Desktop/1-Thesis/[Code]/By Trang/220614_MoveNet/MoveNet_JSON_UR"

charfi_path = "/Users/mac/Desktop/1-Thesis/[Code]/By Trang/220614_MoveNet/MoveNet_JSON_Charfi"
charfi_coffee_room_path = f"{charfi_path}/Coffee_room"
charfi_home_path = f"{charfi_path}/Home"
charfi_lecture_path = f"{charfi_path}/Lecture"
charfi_office_path = f"{charfi_path}/Office"
charfi_office_2_path = f"{charfi_path}/Office_2"

ur_dataset = Dataset(ur_path, 0, 69)
charfi_coffee_room_dataset = Dataset(charfi_coffee_room_path, 0, 69)
charfi_home_dataset = Dataset(charfi_home_path, 70, 129)
charfi_lecture_dataset = Dataset(charfi_lecture_path, 130, 156)
charfi_office_dataset = Dataset(charfi_office_path, 157, 189)
charfi_office_2_dataset = Dataset(charfi_office_2_path, 190, 220)

ur_fall = ur_dataset.fall
charfi_fall = charfi_coffee_room_dataset.fall + \
    charfi_home_dataset.fall + \
    charfi_lecture_dataset.fall + \
    charfi_office_dataset.fall + \
    charfi_office_2_dataset.fall

print(ur_fall)
print(charfi_fall)

# Archived: Move files to folders
# import os
# import shutil
# path = "/Users/mac/Desktop/1-Thesis/[Code]/By Trang/220614_MoveNet/MoveNet_JSON_Charfi/Office_2/"
# start = 190
# end = 220
# list_dir = os.listdir(path)
# for i in range(start, end+1):
#     dest_path = os.path.join(path, f"video_{i}")
#     os.mkdir(dest_path)

#     prefix = f"data {i} ("
#     for item in list_dir:
#         if item.startswith(prefix):
#             item_path = os.path.join(path, item)
#             shutil.move(item_path, dest_path)
