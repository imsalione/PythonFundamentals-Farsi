import hashlib
import os

def hash_file(filename):
    h = hashlib.sha1()
    
    with open(filename, 'rb') as file:
        chunk = 0
        
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
            
    return h.hexdigest()

folder_name = 'src'
file_name = 'BikeData.csv'
file_path = os.path.join(folder_name, file_name)

message = hash_file(file_path)
print(message)