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

# Change the work directory to the root of the repository
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("..")

if os.path.exists("pull_request_body.txt"):
    # Get the pull request body
    with open("pull_request_body.txt", "r", encoding="utf-8") as f:
        body = f.read()
        print("Pull request body: \n" + body)

    # Get the list of files that have been deleted and delete them
    for file in re.findall(r"deleted by us:\s+(.+?)\n", body):
        if os.path.exists(file) and os.path.isfile(file):
            os.remove(file)
            print(f"Delete file: {file}")

    # Remove the pull request body file
    os.remove("pull_request_body.txt")
