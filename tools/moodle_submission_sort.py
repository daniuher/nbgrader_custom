# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 10:19:59 2020

@author: duher18
"""


# autograde test

import zipfile
import os
import shutil
from datetime import datetime

# filename = input('file: ')
filename = input('Name of the zip file: ')

filepath = os.getcwd()+'\\submitted'
fileitself =  filepath+'\\'+filename
if not os.path.isdir(filepath+'\\extracted'):
    os.mkdir(filepath+'\\extracted')

assignment_name = filename.split('-')[1]+'-'+filename.split('-')[2]

timestamps = list()
with zipfile.ZipFile(fileitself, 'r') as zip_ref:
    for sub in zip_ref.infolist():
        timestamps.append(sub.date_time)
    zip_ref.extractall(filepath+'\\extracted')
# os.remove(filepath)
extractedpath = filepath+'\\extracted'

submissions = os.listdir(extractedpath)
# submissions = [submission for submission in submissions]

for submission in submissions:
    
    temp_path = extractedpath+'\\'+submission # path to the extracted submission weird-name folder
    temp_filezip = os.listdir(temp_path)[0] # submitted_file.zip
    temp_file = temp_filezip.split('.')[0] # submitted_file 
    assignment_number = temp_file.split('_')[1] 
    student_number = temp_file.split('_')[2]
     
    
    if not os.path.isdir(filepath+'\\'+student_number):
        os.mkdir(filepath+'\\'+student_number)
    
    student_path = filepath+'\\'+student_number
    if not os.path.isdir(student_path+'\\'+assignment_name):
        os.mkdir(student_path+'\\'+assignment_name)
        
    # timestamp   
    
    # timestamp = os.path.getmtime(temp_path+'\\'+temp_filezip)
    # timestamp = datetime.fromtimestamp(timestamp)
    timestamp = timestamps.pop(0)
    timestamp = datetime(*timestamp[0:])
    text_file = open(student_path+'\\'+assignment_name+'\\'+"timestamp.txt", "w")
    text_file.write(str(timestamp))
    text_file.close()
        
    
    with zipfile.ZipFile(temp_path+'\\'+temp_filezip, 'r') as zip_ref:
        zip_ref.extractall(student_path+'\\'+assignment_name)
    
    
    
    os.remove(temp_path+'\\'+temp_filezip)
    shutil.rmtree(temp_path)
    
os.rmdir(extractedpath)    
    # temp_path = temp_path+'\\'+student_number
    # if not os.path.isdir(temp_path):
    #     os.mkdir(temp_path)
    