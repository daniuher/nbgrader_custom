# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 05:21:58 2020

@author: duher18
"""


config_raw = """c = get_config()

#------------------------------------------------------------------------------
# AssignLatePenalties(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## Preprocessor for assigning penalties for late submissions to the database

## The plugin class for assigning the late penalty for each notebook.
# c.AssignLatePenalties.plugin_class = 'nbgrader.plugins.latesubmission.LateSubmissionPlugin'
c.AssignLatePenalties.plugin_class = 'late.SubMarks'

#------------------------------------------------------------------------------
# ClearSolutions(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## The delimiter marking the beginning of a solution
c.ClearSolutions.begin_solution_delimeter = '# ---------- YOUR CODE STARTS HERE -----------'

## The code snippet that will replace code solutions
c.ClearSolutions.code_stub = {'python': '# ---------- YOUR CODE STARTS HERE -----------\\n\\n\\n\\n\\n# ----------- YOUR CODE ENDS HERE ------------', 
                              'matlab': "% YOUR CODE HERE\\nerror('No Answer Given!')", 
                              'octave': "% YOUR CODE HERE\\nerror('No Answer Given!')", 
                              'java': '// YOUR CODE HERE'}

## The delimiter marking the end of a solution
c.ClearSolutions.end_solution_delimeter = '# ----------- YOUR CODE ENDS HERE ------------'

"""

with open("nbgrader_config_new.py", "w") as config_file:
    config_file.write(config_raw)