import os

folder_name = 'SampleProjects/src'
file_name = 'data.txt'
file_path = os.path.join(folder_name, file_name)

file_stat = os.stat(file_path)
print(f"File size : {file_stat.st_size} bytes")