# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:17:01 2020

@author: duher18
"""

import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

from nbgrader.api import Gradebook
from getpass import getpass
import os


# --- set the necessary variables
print("""Make sure you are done with all manual grading before sending out the
feedback. If you want to change some manual grading, you can generate
the feedback again. Make sure all grading is final before sending the
feedback to students.""")      

assignment_name = input('Assignment name: ')
my_address = input('Your email: ')
password = getpass('Password: ')

smtpsrv = "smtp.office365.com"
smtpserver = smtplib.SMTP(smtpsrv,587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.login(my_address, password)




feedback_folder = os.getcwd()+'\\feedback'

with Gradebook('sqlite:///gradebook.db') as gb:
    
    feedback_students = os.listdir(feedback_folder)    
    
    for student_id in feedback_students:
        
        # --- setup the message ---
        msg = MIMEMultipart()
        # assignment_name = 'A1-Imaging'
        
        msg['Subject'] = 'MV_'+assignment_name.split('-')[0]+' Feedback'
        
        msg['From'] = my_address
        
        body = """
        Hi!
        
        Please find the feedback for the assignment {} attached.
        
        Best regards,
        Teacher
        
        
        """.format(assignment_name)
        student = gb.find_student(student_id)
        msg['To'] = student.email
        student_feedback = feedback_folder+'\\'+str(student.id)+'\\'+assignment_name        
        
        if os.path.isdir(student_feedback):
            
            fdb_name = [ x for x in os.listdir(student_feedback) if ".html" in x ]
            student_feedback = student_feedback+'\\'+fdb_name[0]
            print('Sending feedback to '+student.first_name+' '+student.last_name+' '+str(student.id)+' ...')
                
            # --- attach the feedback
            msg.attach(MIMEText(body, 'plain')) 
            filename = fdb_name[0]
            attachment = open(student_feedback, "rb") 
            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read()) 
            encoders.encode_base64(p) 
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
            msg.attach(p)
            
            
            # --- create connection and send
            smtpserver.send_message(msg)
        
    
    
    gb.close()
    
smtpserver.close()    
print('All available feedbacks were sent succesfully!')    
