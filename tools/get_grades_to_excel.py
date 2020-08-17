# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 08:49:01 2020

@author: duher18
"""



from nbgrader.api import Gradebook, MissingEntry
import xlsxwriter



def addHeaderToXcel(workbook, worksheet):
    """
    This function adds the header to the grades excel file.
    """
    
    # make the header
    header = ['Name', 'Student ID']+[worksheet.get_name()]
    
    
    # set bold text format
    bold = workbook.add_format({'bold': True})
    
    
    # cycle through the header and add it to the first row
    for i in range(len(header)):
        worksheet.write(0, i, header[i], bold)





workbook = xlsxwriter.Workbook('grades_test.xlsx')

# Create the connection to the database
with Gradebook('sqlite:///gradebook.db') as gb:

    grades = []

    # Loop over each assignment in the database
    for assignment in gb.assignments:
        
        assignment_id = assignment.name.split('-')[0]
        worksheet = workbook.add_worksheet(assignment_id)
        addHeaderToXcel(workbook, worksheet)
        row = 1
        
        # Loop over each student in the database
        for student in gb.students:
            
            row += 1
            # Create a dictionary that will store information about this student's
            # submitted assignment
            
            # score = {}
            # score['max_score'] = assignment.max_score
            # score['student'] = student.id
            # score['assignment'] = assignment.name

            # Try to find the submission in the database. If it doesn't exist, the
            # `MissingEntry` exception will be raised, which means the student
            # didn't submit anything, so we assign them a score of zero.
            try:
                submission = gb.find_submission(assignment.name, student.id)
            except MissingEntry:
                # score['score'] = 0.0
                sc = 'not submitted'
            else:
                # score['score'] = submission.score
                sc = submission.score

            # grades.append(score)
            
            worksheet.write(row,1, student.id)
            worksheet.write(row,2, sc)
    
    workbook.close()
    # Create a pandas dataframe with our grade information, and save it to disk
    
    # grades = pd.DataFrame(grades).set_index(['student', 'assignment']).sortlevel()
    # grades.to_csv('grades.csv')

    # # Print out what the grades look like
    # with open('grades.csv', 'r') as fh:
    #     print(fh.read())