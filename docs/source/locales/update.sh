#!/bin/sh
# update transifex pot and local po files

set -ex

# required environment variables
# SPHINXINTL_TRANSIFEX_USERNAME=haiiliin
# SPHINXINTL_TRANSIFEX_PROJECT_NAME=abqpy


# pull po files from transifex
cd `dirname $0`
cd ..
# sphinx-intl create-transifexrc
#rm -R pot  # skip this line cause "already unused pot files will not removed" but we must keep these files to avoid commit for only "POT-Creation-Time" line updated. see: https://github.com/sphinx-doc/sphinx/issues/3443
sphinx-build -T -b gettext . locales/pot
sphinx-intl update -p locales/pot -l zh_CN
# cat .tx/config
# tx push -s --skip
# rm -R -f zh_CN
# tx pull -l zh_CN
# git checkout .tx/config
