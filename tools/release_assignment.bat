@echo off
set p=C:\Anaconda3
call %p%\Scripts\activate.bat %p%
call conda activate cmvs
call python print_assignments.py
call python release_assignment.py
pause