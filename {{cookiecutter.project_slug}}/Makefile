# Used to execute all in one shell
.ONESHELL:

pyexec = python{{cookiecutter.development_python_version}}
pypoetry = $(pyexec) -m poetry

# Upgrade poetry, setup for installation
setup:
	$(pyexec) -m pip install --upgrade poetry

# Install project in production mode
install-production: setup
	$(pypoetry) install --no-dev

# Setup the project firstly
firstly-init: setup
	git init && \
	git remote add origin https://github.com/{{cookiecutter.github_project_name}} && \
	git checkout -b gh-pages
	git commit --allow-empty -m "Initial commit fo GH Pages"
	git push origin gh-pages -f
	git checkout -b {{cookiecutter.github_main_branch}}
	make install-dev-all

# Install project in development mode
install-dev-all: setup
	$(pypoetry) install -E dev-all && $(pypoetry) run pre-commit install

# Install project with dev style dependencies
install-dev-style: setup
	$(pypoetry) install -E dev-style && $(pypoetry) run pre-commit install

# Install static checkers (i.e. mypy)
install-dev-check: setup
	$(pypoetry) install -E dev-check

# Install docs builder dependencies
install-dev-docs: setup
	$(pypoetry) install -E dev-docs

# Install tests tools
install-dev-test: setup
	$(pypoetry) install -E dev-test

# Reformat code style
format:
	$(pypoetry) run black {{ cookiecutter.project_slug }} && \
	$(pypoetry) run isort {{ cookiecutter.project_slug }} && \
	$(pypoetry) run autoflake \
		--ignore-init-module-imports \
		--remove-unused-variables \
		--recursive \
		--in-place {{ cookiecutter.project_slug }} tests

# Run tests local 
test:
	$(pypoetry) run pytest tests --cov={{cookiecutter.project_slug}} --cov-report=html

# Tests command for CI with .coveragerc report
test-ci:
	$(pypoetry) run coverage run --source={{cookiecutter.project_slug}} -m pytest tests

# Serve coverage report
serve-cov:
	python -m http.server -d htmlcov -b 127.0.0.1

# Run hot-reloaded docs server
serve-docs:
	$(pypoetry) run mkdocs serve

# Deploy docs command
deploy-docs:
	$(pypoetry) run mike deploy --push --update-aliases 0.1 latest

# Run mypy checking
check:
	$(pypoetry) run mypy
