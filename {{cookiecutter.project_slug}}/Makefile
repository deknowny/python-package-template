# Used to execute all in one shell
.ONESHELL:

pypoetry = python{{cookiecutter.development_python_version}} -m poetry

# Upgrade poetry, setup for installation
setup:
	python{{cookiecutter.development_python_version}} -m pip install --upgrade poetry
	$(pypoetry) config virtualenvs.in-project true --local

# Install project in production mode
install-production: setup
	$(pypoetry) install --no-dev

# Install project in development mode
install-dev-all: setup
	$(pypoetry) install -E dev-all && $(pypoetry) run pre-commit install

# Install project with dev style dependencies
install-dev-style: setup
	$(pypoetry) install -E dev-style && $(pypoetry) run pre-commit install

# Install static checkers (i.e. mypy)
install-dev-check: setup
	$(pypoetry) install -E dev-check && $(pypoetry) run pre-commit install

# Install tests tools
install-dev-test: setup
	$(pypoetry) install -E dev-test && $(pypoetry) run pre-commit install

# Reformat code style
format:
	$(pypoetry) run black {{ cookiecutter.project_slug }} && \
	$(pypoetry) run isort {{ cookiecutter.project_slug }}

# Run tests local 
test:
	$(pypoetry) run pytest tests --cov={{cookiecutter.project_slug}} --cov-report=html

# Tests command for CI with .coveragerc report
test-ci:
	$(pypoetry) run coverage run --source={{cookiecutter.project_slug}} -m pytest tests

# Serve coverage report
serve-cov:
	python -m http.server -d htmlcov -b 127.0.0.1
