@echo off
call conda activate nbgrader_env
call python "%cd%\tools\send_feedback_to_students.py"
pause