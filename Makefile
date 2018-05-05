yapf:
	yapf -r -i bplot/

doc:
	$(MAKE) -C doc html
