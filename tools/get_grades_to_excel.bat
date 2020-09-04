@echo off
call conda activate nbgrader_env
call python "%cd%\tools\get_grades_to_excel.py"
pause