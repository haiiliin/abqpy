#!/bin/sh
# update local po files

set -ex
cd "$(dirname "$0")"
pdm run sphinx-build -T -b gettext -j auto source source/locale/$version/pot
pdm run sphinx-intl update -p source/locale/$version/pot -l zh_CN
pdm run pofmt || true
