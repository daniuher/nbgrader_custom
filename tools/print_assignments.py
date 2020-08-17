# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:32:37 2020

@author: duher18
"""


from tabulate import tabulate
import textwrap
import os

def getAssignments():
    
    assignments = os.listdir(os.getcwd()+"\\source")
    unwanted = ['.ipynb_checkpoints', 'header.ipynb']
    
    for assignment in assignments:
        if assignment in unwanted:
            assignments.remove(assignment)
                
    return assignments
    
def getReleasedAssignments():
    
    source_assignments = getAssignments()
    released = os.listdir(os.getcwd()+"\\release")
    unwanted = ['.ipynb_checkpoints', 'header.ipynb']
    
    for assignment in released:
        if assignment in unwanted:
            released.remove(assignment)
        if assignment not in source_assignments:
            released.remove(assignment)
            
    return released




assignments = getAssignments()
released = getReleasedAssignments()

to_be_printed = []
for assignment in assignments:
    if assignment in released:
        a = list([assignment, u'\u221a'])
    else:
        a = list([assignment, 'x'])    
    to_be_printed.append(a)    

print(' ')
print('              Available assignments')
print(' ')
table = tabulate(to_be_printed, headers=['Assignment', 'Already released?'], tablefmt="psql", colalign=("left","center"))
print(textwrap.indent(table, 4*' '))
print(' ')




