#!/usr/bin/env bash
apt-get install -y python3 python3-pip python3-dev jq

pip3 install nbgrader numpy matplotlib
# Update these back to the latest versions
pip3 install jupyter-console ipython

# This is for GradeScope
pip3 install -r /autograder/source/requirements.txt

cp /autograder/source/nbgrader_config.py /autograder
cp /autograder/source/source/header.ipynb /autograder/
cp -r /autograder/source/source/pf2 /autograder/
