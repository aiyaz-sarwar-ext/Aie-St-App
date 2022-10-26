#!/bin/sh

set -e
set -u
set -x



wheel=dist/$(ls dist/ | grep --color "whl")

python3 -m twine upload --repository-url ${ARTIFACTORY_REPOSITORY} $wheel --verbose

