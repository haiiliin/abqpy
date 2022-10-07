#!/bin/sh
# update local po files

set -ex
cd `dirname $0`
cd ..
sphinx-build -T -b gettext . locales/pot
sphinx-intl update -p locales/pot -l zh_CN 
