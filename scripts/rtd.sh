#!/bin/sh
# update local po files

set -ex
cd "$(dirname "$0")"

# Activate the current versions and hide the previous ones
for MAJOR in $(seq 2016 2023)
do
    python rtd.py version update --project=$PROJECT --version=v$MAJOR.$MINOR_PATCH $ARGS
done

# Update the redirects to make `20**` point to the latest versions
python rtd.py redirect update --project=$PROJECT --minor_patch="$MINOR_PATCH"
