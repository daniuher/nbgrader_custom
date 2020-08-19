@echo off
set p=C:\Anaconda3
call %p%\Scripts\activate.bat %p%
call conda activate cmvs
call python "%cd%\tools\moodle_submission_sort.py"
pause