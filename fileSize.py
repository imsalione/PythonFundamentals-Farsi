import os
from pathlib import Path

folder_name = "SampleProjects/src"
file_name = "data.txt"
file_path = os.path.join(folder_name, file_name)

# using os module
file_stat = os.stat(file_path)
print(f"File size: {file_stat.st_size} bytes")

print('------------------------------')

# using pathlib module
file = Path(file_path)
print(f"File size: {file.stat().st_size} bytes")