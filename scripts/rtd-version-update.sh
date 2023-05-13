#!/bin/sh
# update local po files

set -ex
cd "$(dirname "$0")"

python rtd.py version update v2023.$VERSION $ARGS --project=$PROJECT
python rtd.py version update v2022.$VERSION $ARGS --project=$PROJECT
python rtd.py version update v2021.$VERSION $ARGS --project=$PROJECT
python rtd.py version update v2020.$VERSION $ARGS --project=$PROJECT
python rtd.py version update v2019.$VERSION $ARGS --project=$PROJECT
python rtd.py version update v2018.$VERSION $ARGS --project=$PROJECT
python rtd.py version update v2017.$VERSION $ARGS --project=$PROJECT
python rtd.py version update v2016.$VERSION $ARGS --project=$PROJECT
