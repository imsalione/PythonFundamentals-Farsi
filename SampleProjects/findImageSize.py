import os

def jepg_res(filename):
    with open(filename,'rb') as img_file:
        
        img_file.seek(163)
        
        a = img_file.read(2)
        
        height = (a[0] << 8) + a[1]
        
        a = img_file.read(2)
        
        width = (a[0] << 8) + a[1]
        
    print("The resolution of the image is", width, "x", height)

folder_name = 'src'
file_name = '512kb.jpg'
file_path = os.path.join(folder_name, file_name)
    
jepg_res(file_path)