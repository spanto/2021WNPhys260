#!/bin/bash

function nbvalidate_source {
    # validate new source notebook.  Expects argument like pf1, ps1, etc.
    nbgrader validate source/$1/*.ipynb
}

function nbgenerate {
    # generate new assignment. Expects argument like pf1, ps1, etc.
    eval assignment_name="$1"
    nbgrader generate_assignment $assignment_name --IncludeHeaderFooter.header=source/header.ipynb --force
}

function nbvalidate_assignment {
    # validate new source notebook.  Expects argument like pf1, ps1, etc.
    nbgrader validate --invert release/$1/*.ipynb
}

function mv_assignments {
    # move assignments to the appropriate student id location
    # Expects first argument to be the .ipynb assignment file,
    #   expects second argument to be assignment name (e.g. pf1, ps1)

    assignment_file=$1
    assignment_name=$2
    
    # Collect the uniqname
    uniqname_line=$(grep "UNIQNAME" $1)
    echo "uniqname_line is" $uniqname_line
    # Looks like: "UNIQNAME = \"cavestru\"\n",
    
    # Strip beginning (see http://mywiki.wooledge.org/BashFAQ/073)
    uniqname=${uniqname_line#*\\\"}
    echo $uniqname

    # Strip the end
    uniqname=${uniqname%\\\"*}
    echo $uniqname
    mkdir -p submitted/$uniqname/$assignment_name
    cp $assignment_file submitted/$uniqname/$assignment_name

}

function nbautograde {
    # grade new assignment. Expects argument like pf1, ps1, etc.
    eval assignment_name="$1"
    nbgrader autograde $assignment_name --force
    }
