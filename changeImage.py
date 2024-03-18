#!/usr/bin/env python3
###Size: Change image resolution from 3000x2000 to 600x400 pixel
####Format: Change image format from .TIFF to .JPEG
import os
from PIL import Image
listimages_tif=os.listdir('/home/student-04-1c6cbe55ad0c/supplier-data/images')
print(listimages_tif)
def change_image(listimages_tif):
        for i in listimages_tif:
                print(i)
                if '.tiff' in i:
                        file_path=os.path.join('/home/student-04-1c6cbe55ad0c/supplier-data/images',i)
                        im=Image.open(file_path)
                        print("the format is",im.format)
                        print("the size is",im.size)
                        print("the mode is",im.mode)
                        img=im.convert('RGB').resize((600,400)).save(file_path.strip('.tiff')+'.jpeg','JPEG')
                        print(img)
change_image(listimages_tif)
