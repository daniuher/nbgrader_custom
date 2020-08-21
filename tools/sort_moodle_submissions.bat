@echo off
call conda activate nbgrader_env
call python "%cd%\tools\moodle_submission_sort.py"
pause