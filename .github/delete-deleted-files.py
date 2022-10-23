"""
Deleted conflicted deleted files from a git repository from the cherry-pick output. For example:

On branch mergify/bp/V2017/pr-993
Your branch is up to date with 'origin/V2017'.

You are currently cherry-picking commit 16e1200.
  (fix conflicts and run "git cherry-pick --continue")
  (use "git cherry-pick --skip" to skip this patch)
  (use "git cherry-pick --abort" to cancel the cherry-pick operation)

Unmerged paths:
  (use "git add/rm <file>..." as appropriate to mark resolution)
	deleted by us:   src/abaqus/PredefinedField/Field.py
	deleted by us:   src/abaqus/PredefinedField/FieldState.py
"""

import os
import re
import sys

# Change the work directory to the root of the repository
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir('..')

# Get the pull request body
pr_body = sys.argv[1]

# Get the list of files that have been deleted and delete them
for file in re.findall(r"deleted by us:\s+(.+?)\n", pr_body):
    os.remove(file)
    print(f"Deleted file: {file}")
