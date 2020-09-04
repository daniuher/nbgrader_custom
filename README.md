# nbgrader toolbox

### UPDATES
**3.9.2020 send feedback to students implemented**
> from now on, generated feedback will be sent to corresponding students via email
> by clicking the send_feedback_to_students.bat and specifying the assignment

**31.8.2020 moodle submission progress**
> Moodle can collect only zip files, therefore moodle sort has been adjusted to that
> plus it is now possible to sort group submission plus incorrectly named submissions

**27.8.2020 assignment pull adjusted**
> in order to be able to pull the assignments, you need to be a collaborator in the repository. 
> Free github supports only three collaborators and currently there are two. Therefore, if similar system
> is to be used in the future, a different method needs to be setup (gitlab, etc.)

**26.8.2020 nbgrader_env automatic now**
> the creation of the nbgrader_env is from now on automatic. If the environment has already been created, the installer will ask, if you want 
> to recreate it. It is recommended to choose *(y)* and recreate the environment. 



The **nbgrader_toolbox** provides a couple fo Python scripts with some linked excutable *.bat* files,
through which we can easily manipulate the nbgrader ecosystem.

[nbgrader](https://github.com/jupyter/nbgrader) is an open-source software systen for assigning and grading Jupyter notebooks. 
nbgrader has a rich working environment and is operable through either commandline or
a GUI Jupyter extension called Formgrader. [nbgrader's official documentation](https://nbgrader.readthedocs.io/en/stable/)
provides a overview of the application and how to use it in its vanilla form.

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

## Installation
Upon installing conda, proceed as follows:

1. Clone this repository or download it as a zip file and extract the downloaded archive.
2. Double-click the executable `install_nbgrader.bat`

Done!


Upon installation, the following hierarchy will get created:
- install_nbgrader.bat
- nbgrader (folder)
	- create_course_folder.bat
	- tools
		- ***(.bat files)***
			- add_or_update_students.bat
			- autograde_assignment.bat	
			- launch_jupyter.bat
			- pull_assignments.bat
			- release_assignment.bat
			- sort_moodle_submissions.bat
			- update_grades_file.bat

		- ***(.py files)***
			- add_or_update_students.py
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

## Uninstall 

- Open the anaconda prompt 
- use the following command to remove the environment with nbgrader 
	```sh
	\> conda remove --name nbgrader_env --all
	```
- Go to your Anaconda3 folder (usually located on C drive alongside the Documents, Desktop, etc. folders. Or directly in C next the Program files folder) <br />
- Within Anaconda3 folder, go to `Anaconda3 -> envs` and delete the *nbgrader_env* folder and the *.conda_envs_dir_test*


## Reinstall

Should you accidentaly lose or delete the tools, they can be downloaded/cloned from this repository from the *installer* branch.

Follow the uninstall guide above and then install a fresh new installation following the installation guide above.


# Orientation

## Create course folder
![Create course folder](https://github.com/daniuher/nbgrader_toolbox/blob/master/doc/create_course_folder.gif)

1. Within the nbgrader folder, doublie-click the `create_course_folder.bat` file. 
2. A commandline window will appear. 
3. Select a name for the course. It doesn't matter what the names is.
4. You will be asked if you want to download the assignments from our private repository. 
Choose *y*. Course ID will be required. You will be prompted for the username and password and if you are
not a collaborator, you will not be able to clone the assignments. If you are a collaborator and managed
to eneter your credentials wrong, you need to remove them from 
Control Panel > User Accounts > Credential Manager > Windows Credentials

The created course root folder can be stored wherever on the computer, however the file hierarchy within the course root folder
needs to remain unchannged and is to be followed. <br /> <br />
**Source** folder
> Containg the master versions of the assignments. The master versions are created according to the [official documentation](https://nbgrader.readthedocs.io/en/stable/user_guide/creating_and_grading_assignments.html)

**Release** folder
> Containing all the assignments, that have been released (= the student versions of the assignments.)

**Submitted** folder
> Contains all the submissions by the students. 


These folders have to follow a strict hierarchy established by the *nbgrader* original application. 
More information about the hierarchy [here](https://nbgrader.readthedocs.io/en/stable/user_guide/philosophy.html)

Everything within the nbgrader course is stored in the **gradebook.db** database file. This file contains all the information
about the students, their grades, the assignments and so on. <br />
WARNING! This file might not be created immediately, when you create the course folder, however it will get generated after we do our first necessary operations.

## Step-by-step operating guide
1. Synchronize the students with Moodle
2. Release an assignments, or in other words, generate the student version.
3. Upload the released version into Moodle.
4. Collect student submission.
5. Sort the submission.
6. Autograde assignment.
7. Check them manually, grade manual tasks.
8. Upgrade the grades .csv file
9. Upload grades to Moodle.
10. Generate feedback for the graded assignments.
11. Send feedback to students via email.


### Synchronize the students
> We need to synchronize the students, that are enrolled in our Moodle with the student list stored within the **gradebook.db** file.
1. Go to the Moodle course page.
2. Change the Moodle interface language to English. IMPORTANT. It won't work otherwise. 
3. Click **Participants** in the right vertical menu.
4. Select all the participants, however exclude the teachers and leave only students selected.
5. In the roll-down menu below the participants list, select **Download table data as** *comma seperated values .csv*
6. Locate the downloaded .csv file and move/copy it into the course root folder, that we created earlier.
7. Within the course folder, double-click the **add_or_update_students.bat**. 
8. You can either rename the downloaded participants file to **participants.csv**, in which case the the file will get recognized automatically, or just copy/paste the name of the downloaded .csv file to the commands line. Hit enter. 


You should see all the students that have been added listed in the command-line. 

**Check the course and the students**
> When done importing the students, let's check the course through the nbgrader Formgrader extension for Jupyter.

1. Within the course folder, double-click **launch_jupyter.bat**.
2. In Jupyter, click the **Formgrader**, the last item in the top horizontal menu.
3. In Formgrader, we can now see the available assignments, that are stored in the *source* folder. These assignments are not stored in the *gradebook.db* file yet,
they are simply listed as detected assignments. 
4. In the vertical menu on the left side, select **Manage students**. 
5. We should now see a complete list of the students corresponding to the one in Moodle.


### Release an assignment
> We want to generate the student version of the master assignment. Meaning, we want to remove all the tests, solutions and leave blank spaces for the students to fill in. 

1. In the course folder, double-click **release_assignment.bat**. It will list all the available assignments in a table on top.
2. Write, which assignments you wish to release. You have to write the full name of the assignment.
3. Provide the due date within the format that is specified. *YYYY-MM-DD HH:MM:SS*. Make sure the due date is the same as in the Moodle page for the assignment.
4. The released assignment is stored in the *release* folder. 
5. Archive the released files and upload them to Moodle.

### Sort Moodle submissions
!! We are collecting only the *.ipynb* files.
> After the deadline, let's collect the submissions as follows:

1. Within the moodle course page, set the interface language to English in the top roll-down menu.
2. Go to the assignment page.
3. Select all the submissions and select **Download selected submissions**.
4. Locate the downloaded archive and move into the **submitted** subfolder. **coursef_root_folder/submitted**.
5. Copy the name of the downloaded archive. Don't change the name!
6. In the course root folder, double-click the **sort_moodle_submissions.bat**.
7. Paste the name of the submission archive and hit Enter. 
8. We should have the archive now extracted according to the hierarchical rules. 
9. Delete the archive file.
<br />
In Jupyter (launch_jupyter.bat if closed), we can now see that for the assignment, a number of submissions have been added. 

### Autograde submissions
> Upon collection the submission, the next step is to autograde them

1. In the course folder, select **autograde_assignemt.bat**. 
2. Write, which assignment is to be autograded, and hit Enter.

<br />
The autograding might take some time. It needs re-insert all the tests, run the noteboks and store everything in the database. 

### Manual grading
> After autograding

1. Launch Jupyter. (*launch_jupyter.bat*)
2. Select Formgrader in the top menu.
3. Select **Manual Grading** in the left vertical menu.
4. Select the assignment, then notebook and click the first submission.
5. If we scroll-down to the sections, which were supposed to be filled by the students, we can see, that
we can now provide a comment under the particular cell. 
6. In the test cells, we can assign the points in the blue top bar. They have been assigned automatically, however we can change them however we want. 
7. Once done with grading the submission, move to the next one by clicking *next* in the top right corner. 

For more information about manual grading and the assignments themselves, please read thorugh [Creating and grading assignments](https://nbgrader.readthedocs.io/en/stable/user_guide/creating_and_grading_assignments.html) in the nbgrader official documentation.

### Upload grades to Moodle
> After finishing our grading, we want to upload the grades to the course in Moodle. We will export a grades file, update the grades in it, and import it back to Moodle.

1. Go to the Moodle course page and change the language to English.
2. In the right vertical menu, select **Course grading**.
3. In the top horizontal menu, select **Export**.
4. In the secondary horizontal menu, select **Plain text file**.
5. Leave checked only the assignment, which has been currently autograded.
6. Click **Download**.
7. Locate the downloaded file and move it into the course root folder.
8. In the course folder, double-click **update_grades_file.bat**.
9. Copy/paste or write the names of the .csv grades file and hit Enter.
10. The grades within the file have now been updated. 
11. Go back to the Moodle course page, change language to English and go to **Course Grading**.
12. In the top horizontal menu, select **Import**.
13. Insert the grades .csv file, leave everything as is by default and hit **Upload grades**.
14. Unfortunately, Moodle assigns its own ID numbers for the students, so the UniOulu ID will not match.
Therefore, make sure to set the mapping **Email address** map to **Email address**. That way, the students
will identified by email, which should be also unique for each student.
15. Map the Assignment column to the grades for the corresponding assignment and upload.

### Generate feedback
> Once graded, we want to generate feedback, which will also show if the assignment was submitted late. 

**Formgrader approach**
1. Within **Formgrader** in Jupyter, under the *Manage assignments* tab, select the **Generate feedback** icon.
2. A subfolder *feedback* within the course folder will get created holding the feedback for all the students.

**File approach**
1. Within the course folder, double-click the **generate_feedback.bat**.
2. In the command line window, specify the assignment, for which assignment you want to generate the feedback for.<br />
*Please make sure that the grading (manual and auto) is final before generating the feedback.*

### Send feedback to students
> After generating the feedback, we want send the feedback *.html* file to the corresponding students.
> Unfortunately Moodle cannot accept file feedbacks, so the feedback needs to be sent through email.

1. Within the course folder, double-click the **send_feedback_to_students.bat**.
2. Specify the assignment, for which you want the feedback to be sent out.
<br />
*Again, make very sure that grading is final.*<br />
