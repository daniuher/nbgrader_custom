@echo off
call conda activate nbgrader_env
set /p assignment="Which assignment to autograde? "
call nbgrader autograde %assignment%
pause