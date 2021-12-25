!!! Hint
    If you are familiar with `make`, you can skip it

We are ready for developing but before let's talk a little about `make` and `Makefile`.

`make` the first purpose is simplify build code of C-family languages because commands developers
use with compiler quite long and can contain some boilerplate parts.

But actually `make` can be viewed as commands shortcuts tool for Python too. Perhaps you see `scripts/` folder in different open source projects, and `Makefile` is a pretty replacement for this. It's easier to customize python & poetry version and easier to read & edit scripts code with it. It's like an `npm run` or `yarn run` logic.

For example, instead of running this all the time (it makes your code prettier i.e. remove excess indentations, sorting imports...):
```shell
python -m poetry run black {{ cookiecutter.project_slug }} && \
	git add -u && \
	python -m poetry run isort {{ cookiecutter.project_slug }} && \
	git add -u && \
	python -m poetry run autoflake \
		--ignore-init-module-imports \
		--remove-unused-variables \
		--recursive \
		--in-place {{ cookiecutter.project_slug }} tests
```
You can just run this:
```shell
make format
```

So the template contains many useful shortcuts in `Makefile`. They are full commented, so you can just read everything about them [from source code of the Makefile](https://github.com/deknowny/python-package-template/blob/main/%7B%7Bcookiecutter.project_slug%7D%7D/Makefile) or just in `Makefile` generated in your project. They all are discussed at the corresponding sections.
