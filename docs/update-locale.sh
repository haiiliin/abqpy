#!/bin/sh
# update local po files

set -ex
cd "$(dirname "$0")"
sphinx-build -T -b gettext -j auto source source/locale/$version/pot
sphinx-intl update -p source/locale/$version/pot -l zh_CN
pofmt || true
