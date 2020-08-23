@echo off
rmdir /s /q "%cd%\source"
mkdir "%cd%\source"
call conda activate nbgrader_env
call python "%cd%\tools\git_assignments.py"
xcopy /S "%cd%\assignments" "%cd%\source"
rmdir /s /q "%cd%\assignments"
pause