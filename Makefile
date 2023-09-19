.PHONY: install
install:
	@pip3 install setuptools
	@pip3 install twine

.PHONY: publish
create:
	@python3 setup.py sdist
	@twine upload dist/*