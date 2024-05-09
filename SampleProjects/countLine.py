import os

folder_name = 'src'
file_name = 'data.txt'
file_path = os.path.join(folder_name, file_name)

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

print(f"Count of lines: {file_len(file_path)}")