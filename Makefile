.PHONY: clean install

clean :
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~'    -exec rm --force {} +
	find . -name '__pycache__'  -exec rm -rd --force {} +

install: install-files clean-git
	sudo ./setup.py install --single-version-externally-managed --compile --force --record /dev/null

develop: clean
	sudo ./setup.py develop

clean-git:
	sudo git clean -fdX
