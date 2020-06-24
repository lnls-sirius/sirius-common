.PHONY: clean install uninstall
PACKAGE_NAME=conscommon

clean-git:
	sudo git clean -fdX

clean: clean-git
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~'    -exec rm --force {} +
	find . -name '__pycache__'  -exec rm -rd --force {} +

uninstall:
	sudo /usr/bin/env python3 -m pip uninstall $(PACKAGE_NAME) -y

install: clean-git
	sudo /usr/bin/env python3 -m pip install .

