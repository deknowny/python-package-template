# Explanation of cookiecutter fields
***
## *__project_name__*
Project name. Used in 
* `README.md`
***
## *__project_slug__*
Project name in snake_case. Used in 
* Root dir folder name
* Project folder name
* `README.md` badges
* `pyproject.toml`
* `Makefile`
* Tests example
***
## *__project_description__*
Project long description (1-2 sentences)
* `README.md`
* `pyproject.toml` as package description
***
## *__author_name__*
Author real name
* `LICENSE`
* `pyproject.toml` as package author
***
## *__author_email__*
Author contact email
* `LICENSE`
* `pyproject.toml` as package author email
***
## *__development_python_version__*
Python version used in developing
* In workflows' jobs on publishing and coverage report
* `pyproject.toml` as package author email
* `Makefile` as package author email
***
## *__min_supported_version__*
* `pyproject.toml`
***
## *__github_project_name__*
GitHub username + project name i.e. `deknowny/python-package-template`
* `README.md` badges
* `pyproject.toml`