# nbgrader toolbox

[nbgrader](https://github.com/jupyter/nbgrader) is an open-source software systen for assigning and grading Jupyter notebooks. 
nbgrader has a rich working environment and is operable through either commandline or
a GUI Jupyter extension called Formgrader. [nbgrader's official documentation](https://nbgrader.readthedocs.io/en/stable/)
provides a overview of the application and how to use it in its vanilla form.

The nbgrader_toolbox provides a couple fo Python scripts with some linked excutable *.bat* files,
through which we can easily manipulate the nbgrader ecosystem.

These custom tools are attempting to simplify the workflow with nbgrader from installation
to daily usage and to provide some tools to implement nbgrader into the courses tought at the University of Oulu.
There are a lot of differences between the differences courses and how their system
of assignments is structured, and so the tools will need to be continuosly updated and
and their funcitonality expanded while they are being tested on various other courses.

Current version of the nbgrader_toolbox is working with the infrastructure of the
Machine Vision course. 



## Requirements 
1. [Conda](https://www.anaconda.com/) is installed on your computer.
2. Python 3.x is used through conda
3. Python is added to the system PATH
4. **Create a virtual environment called *nbgrader_env***. This step is crucial(!) in order to have
all the tools working properly. You can create a new environment or clone existing one, so you don't have
reinstall a lot of the basic packages. For more on how to manage virtual
environments, checkout the [conda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
It is currently done in this manner due to the development purposes
and it wouldn't be good to try and polute the *base* environment with developmental progress. In the
future builds, this mandatory step will be removed and the user will simply choose, which environment
they wish to install the application into. 

## Installation
Upon installing conda and creating **nbgrader_env**, proceed as follows:

1. Clone this repository or download it as a zip file and extract the downloaded archive.
2. Double-click the executable `install_nbgrader.bat`

Done!
<br />
<br />
Upon installation, the following hierarchy will get created:
- install_nbgrader.bat
- nbgrader (folder)
	- create_course_folder.bat
	- tools <br /> <br />
		*(.bat files)*
		- add_or_update_students.bat
		- autograde_assignment.bat
		- add_or_update_students.py
		- launch_jupyter.bat
		- pull_assignments.bat
		- release_assignment.bat
		- sort_moodle_submissions.bat
		- update_grades_file.bat

		*(.py files)*
		- create_custom_config.py
		- get_grades_to_excel.py
		- git_assignments.py
		- late.py		
		- moodle_submission_sort.py
		- old_nbgrader_config.py
		- print_assignments.py				
		- release_assignment.py
		- send_feedback_to_students.py				
		- upload_grades.py




## Toolbox contents

- **Master** branch
	- install_nbgrader.bat 
	- README.md
	
- **Installer** branch
	- tools
		- *various tools* (described in next subsection)
	- create_course_folder.bat

### Tools

All the tools are made easy to operate 

equirements: 

Anaconda installed on the computer with Python 3.x

Guide:

	Simply double-click the file. A folder will be pulled from another git repository with 
	all the tools and files that you need. The assignments for Machine Vision should
	be up to date. 

	As a next step, click the create course folder button, which will create
	the course for Machine Vision. So far, everything is created for the
	Machine Vision purposes. 
