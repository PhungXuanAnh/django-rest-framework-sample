#!/bin/sh

# NOTE: using pre-commit package to manage all git pre-commit, this file is only a sample to add git pre-commit hook manually

list_staged_python_files=$(git diff --name-only --diff-filter=d --staged | grep -E '\.py$' | tr '\n' ' ')

if [ -z "$list_staged_python_files" ]
then
      echo "There no staged file"
else
      # shellcheck disable=SC2086
      PYTHONPATH=$PYTHONPATH:./source/ .venv/bin/pylint --rcfile=.pylintrc $list_staged_python_files
fi

