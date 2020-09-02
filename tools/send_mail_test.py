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


# --- set the necessary variables
print("""Make sure you are done with all manual grading before sending out the
feedback. If you want to change some manual grading, you can generate
the feedback again. Make sure all grading is final before sending the
feedback to students.""")      

# assignment_name = input('Assignment name: ')
assignment_name = 'A1-Imaging'
# my_address = input('Email: ')
my_address = 'duher18@univ.yo.oulu.fi'
# password = getpass('Password: ')
password = 'Ax3Kxw33Ha99'

smtpsrv = "smtp.office365.com"
smtpserver = smtplib.SMTP(smtpsrv,587)



# --- setup the message ---
msg = MIMEMultipart()
# assignment_name = 'A1-Imaging'

msg['Subject'] = 'MV_'+assignment_name.split('-')[0]+' Feedback'

msg['From'] = my_address

body = """
Hi!

Please find the feedback for the assignment {} attached.

Best regards,
Dani


""".format(assignment_name)


with Gradebook('sqlite:///gradebook.db') as gb:
    
    for student in gb.students:
        
        msg['To'] = student.email
        
        # --- attach the feedback
        msg.attach(MIMEText(body, 'plain')) 
        filename = 'damn.txt'
        attachment = open(filename, "rb") 
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read()) 
        encoders.encode_base64(p) 
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        msg.attach(p)
        
        
        
        # --- create connection and send
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.login(my_address, password)
        smtpserver.send_message(msg)
        smtpserver.close()
    
    
    gb.close()
    
    
    
