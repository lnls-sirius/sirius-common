.PHONY: clean install

clean :
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~'    -exec rm --force {} +
	find . -name '__pycache__'  -exec rm -rd --force {} +

install: install-files clean-git
	sudo pip install -r requirements.txt .

develop: clean
	sudo pip install -e .

clean-git:
	sudo git clean -fdX
