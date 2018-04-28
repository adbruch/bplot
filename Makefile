yapf:
	yapf -r -i -e bplot/bplot.py bplot/

doc:
	$(MAKE) -C doc html
