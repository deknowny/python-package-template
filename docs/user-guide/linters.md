A **linter** is a tool to _statically_ analyze your code and report for problems. For example, you have a function that receives 1 argument, but you accidentally passed 2. Such static analyser can report you about problems without running your code.

## `mypy`
Mypy analyze your types for correct usage. It does not allow you to do something like `"2" + 2` and prevents many bugs by your typing hints in classes and functions

You can run mypy analyzing with `make check` command. There are will be issues in output if problems exist.

***
As for me, `mypy` is enough. You can also view these as an alternative

* `pyre`
* `pyright`

Or check out linters with purpose of style reports

* `flake8`
* `pylint`

(I put here only what I have ever used and have had some experience)