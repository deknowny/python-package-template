.ONESHELL:

setup:
	python3.8 -m pip install --upgrade cookiecutter poetry

instance:
	rm -rf ./output
	python3.8 -m cookiecutter . -o output < example_stdin.txt
	@echo "\n\nNew instance created in output/ dir"

instance-init-test: instance
	cd output/testlib && \
	python3.8 -m poetry install && \
	python3.8 -m poetry run python -m pytest tests