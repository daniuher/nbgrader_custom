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
import nbformat
import re
from distutils.dir_util import copy_tree


def getStudentNumberFromNotebook(ntbpath):
    # dig out the student number(s) from the notebook
    
    nb = nbformat.read(ntbpath, as_version = 4)
    stuff = nb.cells[0].source
    for line in stuff.splitlines():
        if 'Student ID:' in line:
            temp_number = re.sub("[^0-9]", "", line)
            student_number = re.findall('.......', temp_number)
            return student_number



def deleteCheckpoints(submissionPath):
    # delete .ipynb_checkpoints
    
    if os.path.isdir(submissionPath+'\\.ipynb_checkpoints'):
        shutil.rmtree(submissionPath+'\\.ipynb_checkpoints')
    
        


# filename = input('file: ')
filename = input('Name of the zip file: ')
misses = 0

filepath = os.getcwd()+'\\submitted'


fileitself =  filepath+'\\'+filename
if not os.path.isdir(filepath+'\\extracted'):
    os.mkdir(filepath+'\\extracted')

assignment_name = filename.split('-')[1]+'-'+filename.split('-')[2]

released_path = os.getcwd()+'\\release'
released_assignment_path = released_path+'\\'+assignment_name
files = os.listdir(released_assignment_path)
correct_name = [ x for x in files if ".ipynb" in x ]
files = [ x for x in files if ".ipynb" not in x ]



timestamps = list()
with zipfile.ZipFile(fileitself, 'r') as zip_ref:
    for sub in zip_ref.infolist():
        if sub.filename.split('/')[-1] == correct_name[0]:
            timestamps.append(sub.date_time)
    zip_ref.extractall(filepath+'\\extracted')
# os.remove(filepath)
extractedpath = filepath+'\\extracted'

submissions = os.listdir(extractedpath)
# submissions = [submission for submission in submissions]

for submission in submissions:
    
    temp_path = extractedpath+'\\'+submission # path to the extracted submission weird-name folder
    deleteCheckpoints(temp_path)
    temp_file_ipynb = os.listdir(temp_path)[0] # submitted_file.ipynb
    temp_file = temp_file_ipynb.split('.')[0] # submitted_file 
    assignment_number = temp_file.split('_')[1] 
    try:
        student_numbers = temp_file.split('_')[2]
    except:
        # no student number provided
        student_numbers = getStudentNumberFromNotebook(temp_path+'\\'+temp_file_ipynb)
                    
        
    timestamp = timestamps.pop(0)
    timestamp = datetime(*timestamp[0:])
    
    # create folder for each student seperetaly
    for student_number in student_numbers:
        
        if not student_number:
            misses += 1
            student_number = 'no_student_ID_'+str(misses)
        
        if not os.path.isdir(filepath+'\\'+student_number):
            os.mkdir(filepath+'\\'+student_number)
        
        student_path = filepath+'\\'+student_number
        if not os.path.isdir(student_path+'\\'+assignment_name):
            os.mkdir(student_path+'\\'+assignment_name)
            
        # timestamp   
        
        # timestamp = os.path.getmtime(temp_path+'\\'+temp_file_ipynb)
        # timestamp = datetime.fromtimestamp(timestamp)
        
        text_file = open(student_path+'\\'+assignment_name+'\\'+"timestamp.txt", "w")
        text_file.write(str(timestamp))
        text_file.close()
        
        
        # Copying the supporting files
        copy_tree(released_assignment_path, student_path+'\\'+assignment_name)
        os.rename(temp_path+'\\'+temp_file_ipynb, temp_path+'\\'+correct_name[0])
        shutil.copy(temp_path+'\\'+correct_name[0], student_path+'\\'+assignment_name+'\\'+correct_name[0])
    
    
    # with zipfile.ZipFile(temp_path+'\\'+temp_file_ipynb, 'r') as zip_ref:
    #     zip_ref.extractall(student_path+'\\'+assignment_name)
    
    
    
    # os.remove(temp_path+'\\'+temp_file_ipynb)
    shutil.rmtree(temp_path)
    
os.rmdir(extractedpath)    
    # temp_path = temp_path+'\\'+student_number
    # if not os.path.isdir(temp_path):
    #     os.mkdir(temp_path)
    