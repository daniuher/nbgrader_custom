@echo off
call conda activate nbgrader_env
call python "%cd%\tools\print_assignments.py"
call python "%cd%\tools\release_assignment.py"
pause