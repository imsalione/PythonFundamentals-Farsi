import os

folder_name = "images"
file_name = "512kb.jpg"
file_path = os.path.join(folder_name, file_name)

def jpeg_res(filename):
    
    # open image for reading in binary mode:
    with open(filename, 'rb') as img_file:
        
        # height of image (in 2 bytes) is at 164th position
        img_file.seek(163)
        
        # read 2 bytes
        a = img_file.read(2)
        
        # calculate height
        height = (a[0] << 8) + a[1]
        
        # next 2 bytes is width
        a = img_file.read(2)
        
        # calculate width
        width = (a[0] << 8) + a[1]
        
    print("The resolution of the image is", width, "x", height)
    
jpeg_res(file_path)