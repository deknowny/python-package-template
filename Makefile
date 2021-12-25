.ONESHELL:

setup:
	python3.8 -m pip install --upgrade cookiecutter poetry

install-docs:
	python3.8 -m pip install -r docs/requirements.txt

deploy-docs:
	mike deploy --push --force --update-aliases 0.1 latest -b gh-pages

instance:
	rm -rf ./output
	python3.8 -m cookiecutter . -o output < example_stdin.txt
	@echo "\n\nNew instance created in output/ dir"

instance-init-test: instance
	cd output/testlib && \
	make install-dev-all && \
	make test && \
	make check && \
	make format && \
	git init

serve-doc:
	python3.8 -m mkdocs serve