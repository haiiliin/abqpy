#!/bin/sh
# update local po files

set -ex
cd "$(dirname "$0")"

for MAJOR in $(seq 2016 2023)
do
    echo "$MAJOR"
    python rtd.py version update --version=v$MAJOR.$MINOR_PATCH --project=$PROJECT $ARGS
done
