#!/usr/bin/env bash

python3 setup.py sdist
python3 setup.py bdist_wheel --universal

VERSION=$(git describe)
twine upload dist/*-${VERSION#v}-*
twine upload dist/*-${VERSION#v}.*
