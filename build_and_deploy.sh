#!/bin/bash

rm -rf cpro.egg-info
rm -rf dist
python3.7 setup.py sdist
twine upload --repository-url https://upload.pypi.org/legacy/ dist/* 


