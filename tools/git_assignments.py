# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 18:21:05 2020

@author: duher18
"""


import git

q = input('would you like to pull the assignments from the git repository? [y/n]')
if q == 'y':
    course_branch = input('Course ID: ')
    print('Downloading from repository...')
    my_repo = git.Repo.clone_from('https://daniuher@github.com/daniuher/course_assignments.git', 'assignments')
    
    try:
        my_repo.git.checkout(course_branch)
    except:
        print('Such course does no exist in our repository.')
else:
    print('OK! You can also use the pull_assignments.bat tool file within the course later.')

