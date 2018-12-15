import shutil
import os, sys
import zipfile
from funcs import write_result
directory =         os.path.join('D:/','DONE_PHOTOS_FROM_FREELANCERS','20181214_links_for_upload') #first source
outcome_directory = directory + r'_unzip'     #output manually cropping photo
files = os.listdir(directory) #list of item in directory
#20180404-215514-e7b65c-9-167-520-042800114006.IMG0685.SNe7b65c.obj.0.1.jpg.oe.jpg.pf.jpg.1350nowm.jpg.1350x.jpg
for i in files:
    s=i.replace('.','-')
    s=s.split('-')
    a=(s[6])
    while len(a)!=14:
        a='0'+a
    l='https://s3.amazonaws.com/img.takeoff/manual/'+i
    text=a+','+l+','+i+','+s[6]+'\n'
    write_result('for_upload_20181214.csv', text)