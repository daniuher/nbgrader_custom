@echo off
call conda activate nbgrader_env
call python "%cd%\tools\add_or_update_students.py"
pause