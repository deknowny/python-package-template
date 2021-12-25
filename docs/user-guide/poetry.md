!!! Hint
    If you are familiar with `poetry`, you can skip it

When you are writing a library you need:

1. Dependencies manager (if your project depends on another libraries)
2. Project builder
3. Tool that publishes the project to PyPI
4. A tool that allows isolating dependencies between projects

And a common solution is:

1. `pip`
2. `setuptools`
3. `twine`
4. `venv`

And it's quite easy solution (but actually it wasn't so clear for me few years ago 😅)
***
## Poetry
Sounds amazing but in fact Poetry is a replacement for all these 4 tools, and it gets it easier and more user-friendly.

It's like a `npm` or `cargo`

So this template uses Poetry for dependency manager, project build, publishing tool and dependencies isolating

Read more about dependencies managing at [Manage dependencies](../reference/manage-dependencies.md)
