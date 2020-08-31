@echo off
call conda activate nbgrader_env
call python "%cd%\tools\upload_grades.py"
pause