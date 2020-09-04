@echo off
call conda activate
call conda create --name nbgrader_env
call conda activate nbgrader_env
call conda install gitpython
call pip install tabulate
call pip install pandas
call pip install opencv-python
call pip install opencv-contrib-python
call pip install matplotlib
call pip install xlsxwriter
call conda install jupyter
call conda install -c conda-forge nbgrader
call jupyter nbextension install --sys-prefix --py nbgrader --overwrite
call jupyter nbextension enable --sys-prefix --py nbgrader
call jupyter serverextension enable --sys-prefix --py nbgrader
git clone https://github.com/daniuher/nbgrader_toolbox.git nbgrader
call cd nbgrader
call git checkout installer
pause