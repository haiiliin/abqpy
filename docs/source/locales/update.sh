#!/bin/sh
# update local po files

set -ex
cd "$(dirname "$0")"
cd ../..
sphinx-build -T -b gettext -j auto source build/gettext
sphinx-intl update -p build/gettext -l zh_CN 
