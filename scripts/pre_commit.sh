#!/bin/sh

list_staged_python_files=$(git diff --name-only --diff-filter=d --staged | grep -E '\.py$' | tr '\n' ' ')

if [ -z "$list_staged_python_files" ]
then
      echo "There no staged file"
else
      PYTHONPATH=$PYTHONPATH:./source/ .venv/bin/pylint --rcfile=.pylintrc $list_staged_python_files
fi

