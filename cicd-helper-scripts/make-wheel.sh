#/bin/sh

set -e
set -u
set -x


rm -rf dist
rm -rf build


python3 setup.py bdist_wheel

