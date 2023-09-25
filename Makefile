.PHONY: install
install:
	@pip3 install -r requirements.txt

.PHONY: publish
publish:
	@python3 setup.py sdist
	@twine upload dist/*