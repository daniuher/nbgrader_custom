@echo off
call conda activate nbgrader_env
call python "%cd%\tools\synchronize_students.py"
pause