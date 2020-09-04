# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 13:12:21 2020

@author: duher18
"""


import pandas as pd
from nbgrader.api import Gradebook
import os

# grade_file_name = input('The grade file .csv from moodle name: ')

# df = pd.read_csv(grade_file_name)

# c = df.columns
# assignment_row = c[6]



# assignment_name = df.columns[6].split(' ')[1]
assignment_name = input('Which assignment: ')
emails = list()
ids = list()
grades = list()

with Gradebook('sqlite:///gradebook.db') as gb:
    
    for student in gb.students:
        try:
            submission = gb.find_submission(assignment_name, student.id)
            if submission.notebooks[0].late_submission_penalty:
                score = submission.score - submission.notebooks[0].late_submission_penalty
            else:
                score = submission.score
            # score = submission.score
        except:
            score = 0
        
        ids.append(student.id)
        emails.append(student.email)
        grades.append(score)
        # df.loc[df['ID number'] == int(student.id), assignment_row] = score
        
    gb.close()
    
# df.to_csv (grade_file_name, index = False, header=True)        

data = {'ID': ids, 'Email address': emails, assignment_name: grades}
df = pd.DataFrame(data)
df.to_csv (os.getcwd()+'\\grades_'+assignment_name+'.csv', index = False, header=True)

