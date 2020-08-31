# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 19:52:39 2020

@author: duher18
"""


import pandas as pd
from nbgrader.api import Gradebook


try:
    df = pd.read_csv('participants.csv')
except:
    print('Could not find the participants.csv file')
    participants_file = input('Please enter the name of the participants file: ')
    df = pd.read_csv(participants_file)


try:
    df['ID number'] = df['ID number'].fillna(0)
        
    
    with Gradebook('sqlite:///gradebook.db') as gb:
        
        a = gb.students
        for student in gb.students:
            gb.remove_student(student.id)
        a = gb.students
        
        for index, row in df.iterrows():
            student_id = int(row['ID number'])
            first_name = row['First name'] 
            last_name = row['Surname'] 
            email = row['Email address']
            
            gb.update_or_create_student(student_id, first_name = row['First name'] , 
                           last_name = row['Surname'] , email = row['Email address'])
            
            print(row['ID number'], row['First name'], row['Surname'], row['Email address'])
            
        gb.close()
        
except:
    print('The .csv file is not in English. Please switch moodle to English and download the student list again.')    
    
# with Gradebook('sqlite:///gradebook.db') as gb:
    
#     for student in gb.students:
#         print(student.id)
#         print(student.first_name)
#         print(student.last_name)