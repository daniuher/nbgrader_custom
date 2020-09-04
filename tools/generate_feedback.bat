@echo off
call conda activate nbgrader_env
set /p assignment="Which assignment you want to generate feedback for? "
call nbgrader generate_feedback %assignment%
pause