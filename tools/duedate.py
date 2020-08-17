# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 22:07:33 2020

@author: duher18
"""


from nbgrader.api import Gradebook, MissingEntry
from datetime import datetime

with Gradebook('sqlite:///gradebook.db') as gb:
    
    for assignment in gb.assignments:
        
        print(assignment.name + '  ' + str(assignment.duedate))
        # gb.update_or_create_assignment(assignment.name, 
        #                                 duedate = datetime(2020, 7, 8, 23, 59))
        