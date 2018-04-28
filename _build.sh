#!/bin/sh

pip install .

sphinx-build -M html "doc/source" "doc/build"
