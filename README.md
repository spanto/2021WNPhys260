This repository contains material and tools to integrate nbgrader with
the preflight and problem sets for Phys 260.  There are some useful
bash functions to shortcut steps for nbgrader, and also to effectively
place student assignments in the correct directories.

# Instructions for assignment creator
- Create/edit the assignments in the source directory
- Use the functions in scripts/nbgrader_funcs.sh to go through the steps of validating the assignment, creating a release version of the assignment, and validating the release version of the assignment.
- Post the release version of the assignment for students to download
- Note, students can either go through the notebook with jupyter notebook locally, or upload to google colab and download the .ipynb


# Instructions for assignment grader
- For each downloaded student ipynb file, use 