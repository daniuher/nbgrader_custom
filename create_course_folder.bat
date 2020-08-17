@echo off
set p=C:\Anaconda3
call %p%\Scripts\activate.bat %p%
call conda activate cmvs
set /p course_name="Enter course name: "
nbgrader quickstart %course_name%
mkdir "%cd%/%course_name%/submitted"
mkdir "%cd%/%course_name%/release"
pause