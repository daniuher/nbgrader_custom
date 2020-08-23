@echo off
call conda activate nbgrader_env
call python upload_grades.py
pause