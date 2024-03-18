#!/usr/bin/env python3
#### upload the modified images to the web server that is handling the fruit catalog. 
import os
import requests
import json
listimages_jpeg=os.listdir('/home/student-04-ef33c690cfe3/supplier-data/images')
url="http://34.125.83.92/upload/"
def image_upload(listimages_jpeg):
        for i in listimages_jpeg:
                if '.jpeg' in i:
                        filepath=(os.path.join("/home/student-04-5cdf15401167/supplier-data/images",i))
                        with open(filepath,'rb') as opened:
                                r=requests.post(url,files={"file":opened})
                                print(r.ok)
                                print(r.status_code)


image_upload(listimages_jpeg)
