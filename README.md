This repository contains material and tools to integrate nbgrader with
the preflight and problem sets for Phys 260.  There are some useful
bash functions to shortcut steps for nbgrader, and also to effectively
place student assignments in the correct directories.

To use the functions in scripts/nbgrader_funcs.sh, execute:
```
source scripts/nbgrader_funcs.sh
```

# Instructions for assignment creator
- Create/edit the assignments in the source directory
- Use the functions in scripts/nbgrader_funcs.sh from the top level directory to go through the steps of validating the assignment, creating a release version of the assignment, and validating the release version of the assignment.
```
nbvalidate_source pf1
nbgenerate pf1
nbvalidate_assignment pf1
```
- Post the release version of the assignment for students to download.
- Note, students can either go through the notebook with jupyter notebook locally, or upload to google colab and download the .ipynb


# Instructions for assignment grader
Note:  Examples below are for the assignment pf1
- For each downloaded student ipynb file, use the mv_assignments from the top level directory. e.g., if you downloaded a student's ipynb file into your Downloads directory, execute the following:
```
mv_assignments ~/Downloads/pf1.ipynb pf1
```
- Use the nbautograde function for the assignment to autograde the autogradeable parts, e.g.
```
nbautograde pf1
```
- Launch jupyter notebook from the top level directory, and click on **Formgrader**
- Click on "# Submissions" for the assignment you want to grade.
- Click on the first student, the notebook, and begin any of the manual grading you need to do.  You can simply click on "Next" to go through all students.
- Once you complete writing in feedback to students, you will want to generate the feedback files and collect grades.
- To generate the feedback files, execute:
```
nbgrader generate_feedback pf1
```
- To collect grades to a file called grades.csv, execute:
```
nbgrader export
```
