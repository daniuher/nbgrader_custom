# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 18:06:55 2020

@author: duher18
"""



from nbgrader.api import Gradebook
from getpass import getpass
import imaplib
import base64
import os
import email
from email.header import decode_header
import webbrowser
import zipfile 
from datetime import datetime


email_user = input('Email: ')
email_pass = getpass(prompt='Password: ')
course_name = 'MV'

port = 993
host = "outlook.office365.com"

mail = imaplib.IMAP4_SSL(host, port)

try:
    mail.login(email_user, email_pass)
    print('Login SUCCESFUL!')
except:
    print('Login FAILED! Probably wrong credentials or password.')