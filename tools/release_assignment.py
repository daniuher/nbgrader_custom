# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 20:54:27 2020

@author: duher18
"""

from nbgrader.apps import NbGraderAPI
from nbgrader.api import Gradebook
from traitlets.config import get_config, Config
from dateutil import parser


# c = get_config()
# # load_subconfig('nbgrader_config.py')


with open ('nbgrader_config.py', 'r') as f:
    to_run = f.read()
    exec(to_run)
    api=NbGraderAPI(config=c)
    f.close()
    
available_assignments = api.get_source_assignments()
print(available_assignments)

ass = input('Which one: ')
dd = parser.parse(input('Due date: YYYY-MM-DD HH:MM:SS '))

with Gradebook('sqlite:///gradebook.db') as gb:
    gb.update_or_create_assignment(ass, duedate=dd)
    
    
api.generate_assignment(ass)