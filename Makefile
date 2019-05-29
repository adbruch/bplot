yapf:
	yapf -r -i bplot/

install:
	python setup.py sdist
	pip install ./dist/bplot-0.2.tar.gz
