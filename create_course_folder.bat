@echo off
set p=C:\Anaconda3
call %p%\Scripts\activate.bat %p%
call conda activate cmvs
set /p course_name="Enter course name: "
nbgrader quickstart %course_name%
mkdir "%cd%\%course_name%\submitted"
mkdir "%cd%\%course_name%\release"
rmdir /s /q "%cd%\%course_name%\source" 
mkdir "%cd%\%course_name%\source"
xcopy /S "%cd%\assignments" "%cd%\%course_name%\source"
python "%cd%\tools\create_custom_config.py"
del "%cd%\%course_name%\nbgrader_config.py"
move "%cd%\nbgrader_config.py" "%cd%\%course_name%"
xcopy /S "%cd%\tools\late.py" "%cd%\%course_name%"
pause