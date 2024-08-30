import os
import shutil

directory = "path/to/your/folder"

for filename in os.listdir(directory):
    extension = filename.split('.')[-1]
    folder_path = os.path.join(directory, extension)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    shutil.move(os.path.join(directory, filename), folder_path)
