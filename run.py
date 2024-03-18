#!/usr/bin/env python3
#####add fruit images and their descriptions from the supplier on the fruit catalog web-server
import os
import requests
import json
url="http://34.125.83.92/fruits/"
listtextfiles=os.listdir('/home/student-04-5cdf15401167/supplier-data/descriptions')
pdfdata=[]
def upload_descriptions(listtextfiles):
        for file in listtextfiles:
#                print(file)
                with open(os.path.join('/home/student-04-5cdf15401167/supplier-data/descriptions',file)) as f:
                        fread=f.readlines()
                        webdict={}
                        pdfdata1=[]
                        for i in fread:
                                print(i)
                                if fread.index(i)==0:
                                        webdict['name']=i.strip()
                                        pdfdata1.append('name'+':'+i.strip())
                                elif fread.index(i)==1:
                                        webdict['weight']=int(i.split()[0].strip())
                                        pdfdata1.append('weight'+':'+i.strip())
                                else:
                                    if fread.index(i)==2:
                                        webdict['description']=i.strip()
                                    else:
                                        webdict['description']=webdict.get('description')+i.strip()
#                                print(file[:-4])
                        webdict['image_name']=file[:-4]+'.jpeg'
                        print(webdict)
#                        print(int(i.split()[0].strip())
                        p={"name":webdict['name'],"weight":webdict['weight'],"description":webdict['description'],"image_name":webdict['image_name']}
                pdfdata.append(pdfdata1)
           #     p=json.dumps(webdict)
                response=requests.post(url,data=p)
                print(response.ok)
                print(response.status_code)
        return pdfdata
pdfdata=upload_descriptions(listtextfiles)
