#!/bin/sh
#
# An example hook script to check the commit log message.
# Called by "git commit" with one argument, the name of the file
# that has the commit message.  The hook should exit with non-zero
# status after issuing an appropriate message if it wants to stop the
# commit.  The hook is allowed to edit the commit message file.
#
# To enable this hook, rename this file to "commit-msg".

# Uncomment the below to add a Signed-off-by line to the message.
# Doing this in a hook is a bad idea in general, but the prepare-commit-msg
# hook is more suited to it.
#
# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# grep -qs "^$SOB" "$1" || echo "$SOB" >> "$1"

# This example catches duplicate Signed-off-by lines.

# test "" = "$(grep '^Signed-off-by: ' "$1" |
# 	 sort | uniq -c | sed -e '/^[ 	]*1[ 	]/d')" || {
# 	echo >&2 Duplicate Signed-off-by lines.
# 	exit 1
# }

#
# Automatically adds branch name and branch description to every commit message.
# reference: https://stackoverflow.com/a/11524807/7639845
#

NAME=$(git branch | grep '*' | sed 's/* //') 
DESCRIPTION=$(git config branch."$NAME".description)

echo "$NAME"': '$(cat "$1") > "$1"
if [ -n "$DESCRIPTION" ] 
then
   echo "" >> "$1"
   echo $DESCRIPTION >> "$1"
fi 
