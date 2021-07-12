build:
	rm -rf build dist
	python3 -m build

publish:
	python3 -m twine upload --repository pypi dist/*
