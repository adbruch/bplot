#!/bin/sh

pip install .

cd doc && make clean && make html
