Poetry's dependencies divide into 2 groups and both of them can be _optional_ or _required_:

* _Development_
* _Production_

_Production_ dependencies are installed when your library is installed by a user (usually package is installed from PyPI)

_Development_ dependencies are installed when your library is installed by a contributor with purpose of adding new feature to your library (always package is installed from source, i.e from GitHub)


!!! Question "How does optional dependencies work?"
    All optional dependencies divide into __groups__ by a developer

    For example, some dependencies are required to build documentation. You can view `dev-docs` group of dependencies in `pyproject.toml`. If you need to install only them as optional you can execute this

    ```shell title="Terminal"
    pip install library[dev-docs]
    ```

    Separate by a comma optional dependencies in brackets (`[]`)

    ***

    Anyway, you do not need to install any development dependencies when you install a package
    from `PyPI` as a user. It's for an example

    Any group from dev dependencies could be also installed with `make` out of library source

    ```shell title="Terminal"
    make install-dev-docs
    ```


??? Question "Why the template does not use `dev-dependencies` section?"
    Because now Poetry does not support `dev-dependencies` with extras.
    The template have many development dependencies and full installation of them
    takes quite long time so division is required

    Check out this:

    * [The reason why extras not support with dev-dependencies](https://github.com/python-poetry/poetry/pull/606#issuecomment-437943927)
    * [Awaiting of extra dev-dependencies troubleshooting](https://github.com/python-poetry/poetry/issues/129#issuecomment-791962947)


### Install the project from source in development mode
`make install-dev-all` will install all development dependencies. If you need only a part of them, check out the `Makefile` and find a command for your purpose

### Install the project from source in production mode
`make install-production` will install only required dependencies and the library should be ready for usage

!!! Feature
    You can add the library code as dependency as [Git Submodule](https://git-scm.com/docs/git-submodule)

# Add a non-optional dependency
For example, you want to add a `requests` as dependency for project, so it should be installed when your library is installed
```shell title="Terminal"
poetry add requests
```
Now when someone installs your library, `requests` will be installed too

# Add an optional dependency
For example, you want to optimize JSON parsing in your project with `orjson` library (as it is written on Rust and requires `rustc`). You can do not force user install `orjson` and keep `orjson` as optional
```shell title="Terminal"
poetry add orjson --optional
```
As it's an optional, you should add it to a special group of optional dependencies.

Your `pyproject.toml` looks like this
```toml title="pyproject.toml"
...
[tool.poetry.dependencies]
orjson = {optional = true, version="^3.6.5"}
...
```

And now add the dependency to a new group. Let's call it `fast-json`
```toml title="pyproject.toml" hl_lines="6"
[tool.poetry.extras]
# Ordinary extra dependencies
all = []

# Fast and optimized JSON parsers
fast-json = ["orjson"]
...
```

It's a good practice to unite all your optional dependencies into a `all` group so add it there too
```toml title="pyproject.toml" hl_lines="3"
[tool.poetry.extras]
# Ordinary extra dependencies
all = ["orjson"]

# Fast and optimized JSON parsers
fast-json = ["orjson"]
...
```
# Add a non-optional dev dependency
```shell title="Terminal"
poetry add pytest --dev
```
`pytest` will be installed every time your library is installed in development mode

# Add an optional dev dependency
```shell title="Terminal"
poetry add pytest-asyncio --optional
```
It looks like optional production dependency, but now we should change `extra` section in another way.

All optional development dependencies groups marked with prefix `dev-`. So our `pytest-asyncio` should be addd in such groups.

Check out `pyproject.toml`. There is an existed group of optional dependencies used for testing (as `pytest-asyncio` too)

```toml title="pyproject.toml" hl_lines="3"
[tool.poetry.extra]
...
dev-test = ["pytest", "pytest-cov", "coveralls", "coverage"]
```

Now put it here

```toml title="pyproject.toml" hl_lines="3"
[tool.poetry.extra]
...
dev-test = ["pytest-asyncio", "pytest", "pytest-cov", "coveralls", "coverage"]
```

***
And there is also a `dev-all` group that need to be modified

```toml title="pyproject.toml" hl_lines="7"
[tool.poetry.extra]
...
dev-test = ["pytest-asyncio", "pytest", "pytest-cov", "coveralls", "coverage"]
...
dev-all = [
    "black", "isort", "pre-commit",
    "pytest", "pytest-cov", "pytest-asyncio"
    "coveralls", "coverage",
    "mypy",
    "bumpversion",
    "autoflake",
    "mkdocs", "mkdocs-material", "mike"
]
```
