@echo off
set p=C:\Anaconda3
call %p%\Scripts\activate.bat %p%
call conda activate cmvs
call conda install jupyter
call conda install -c conda-forge nbgrader
call jupyter nbextension install --sys-prefix --py nbgrader --overwrite
call jupyter nbextension enable --sys-prefix --py nbgrader
call jupyter serverextension enable --sys-prefix --py nbgrader
git clone https://github.com/daniuher/nbgrader_custom.git
pause