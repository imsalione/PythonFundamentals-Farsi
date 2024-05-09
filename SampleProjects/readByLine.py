import os

folder_name = "src"
file_name = "data.txt"
file_path = os.path.join(folder_name, file_name)

with open(file_path) as f:
    content_list = f.readlines()
    
print(content_list)

content_list = [x.strip() for x in content_list]
print(content_list)

print('---------------------------')

with open(file_path) as f:
    content_list = [line.rstrip() for line in f]
    
print(content_list)