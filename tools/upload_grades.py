# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 13:12:21 2020

@author: duher18
"""


import pandas as pd
from nbgrader.api import Gradebook

grade_file_name = input('The grade file .csv from moodle name: ')

df = pd.read_csv(grade_file_name)

c = df.columns
assignment_row = c[6]

# s = pd.Series(['w','ddfg',2590657,'lfdkj@dlkg.fi',2],index=['First name','Surname','ID number','Email address',ass_name])

# df.loc[df['First name'] == 'Essi', ass_name] = 2

# a = df.append(s,ignore_index=True)

assignment_name = df.columns[6].split(' ')[1]

with Gradebook('sqlite:///gradebook.db') as gb:
    
    for student in gb.students:
        try:
            submission = gb.find_submission(assignment_name, student.id)
            score = submission.score - submission.notebooks[0].late_submission_penalty
            # score = submission.score
        except:
            score = 0
            
        df.loc[df['ID number'] == int(student.id), assignment_row] = score
        
    gb.close()
    
df.to_csv (grade_file_name, index = False, header=True)        