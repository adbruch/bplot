#!/bin/sh

pip install .

make clean-doc

make -B doc
