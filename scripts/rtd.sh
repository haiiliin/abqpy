#!/bin/sh
# update local po files

set -ex
cd "$(dirname "$0")"

# Activate the current versions and hide the previous ones
for MAJOR in $(seq 2016 2023)
do
    python rtd.py version update --project=$PROJECT --version=v$MAJOR.$CURRENT_MINOR_PATCH --active --nohidden
    python rtd.py version update --project=$PROJECT --version=v$MAJOR.$PREVIOUS_MINOR_PATCH --hidden
done

# Build the versions
for MAJOR in $(seq 2016 2023)
do
    python rtd.py version build --project=$PROJECT --version=v$MAJOR.$CURRENT_MINOR_PATCH
done

# Update the redirects to make `20**` point to the latest versions
python rtd.py redirect update --project=$PROJECT --minor_patch="$CURRENT_MINOR_PATCH"
